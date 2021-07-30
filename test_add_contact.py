import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Firstname",
                                    middlename="Middlename",
                                    lastname="lastname",
                                    nickname="Nickname",
                                    photo="title.gif",
                                    title="Title",
                                    company="Company",
                                    address="Address",
                                    home="100",
                                    mobile="101",
                                    work="102",
                                    fax="103",
                                    email="email@test.test",
                                    email2="email2@test.test",
                                    email3="email3@test.test",
                                    homepage="http://homepage.test",
                                    bday="10",
                                    bmonth="June",
                                    byear="2000",
                                    aday="11",
                                    amonth="July",
                                    ayear="2001",
                                    address2="Address2",
                                    phone2="104",
                                    notes="Notes"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname=""))
    app.logout()
