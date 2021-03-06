import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.application import Application
from fixture.db import DbFixture


fixture = None
target = None


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return(dbfixture)


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    root_path = os.path.dirname(os.path.abspath(__file__))
    if target is None:
        config_file = os.path.join(root_path, request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseUrl=target["web"]["baseUrl"], photoPath=root_path)
    fixture.session.ensure_login(username=target["web"]["username"], password=target["web"]["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return(request.config.getoption("--check_ui"))


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return(importlib.import_module("data.%s" % module).testdata)


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return(jsonpickle.decode(f.read()))


def load_config(file):
    global target
    if target is None:
        root_path = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(root_path, file)
        with open(config_file) as f:
            target = json.load(f)
    return(target)