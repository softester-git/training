from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Firstname",
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
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
