from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Contact for edit"))
    app.contact.edit_first_contact(Contact(firstname="NewFirstname",
        middlename="NewMiddlename",
        lastname="NewLastname",
        nickname="NewNickname",
        photo="Newtitle.gif",
        title="NewTitle",
        company="NewCompany",
        address="NewAddress",
        home="110",
        mobile="111",
        work="112",
        fax="113",
        email="Newemail@test.test",
        email2="Newemail2@test.test",
        email3="Newemail3@test.test",
        homepage="http://newhomepage.test",
        bday="11",
        bmonth="July",
        byear="2010",
        aday="15",
        amonth="June",
        ayear="2011",
        address2="NewAddress2",
        phone2="114",
        notes="NewNotes"))
