from model.group import Group
from fixture.group import GroupHelper
import os.path
import json


testdata = [Group(name="", header="", footer="")] + [Group(name=GroupHelper.random_string("name", 10), header=GroupHelper.random_string("head", 20), footer=GroupHelper.random_string("foot", 20))
                                                     for i in range(5)]
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")
with open(file, "w") as fd:
    fd.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
