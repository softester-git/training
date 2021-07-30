import unittest
from contact import Contact
from application import Application


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Firstname",
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
        self.app.logout()

    def test_add_empty_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="", middlename="", lastname="", nickname=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
