def test_contact_home_page_eq_edit_page(app, db):
    contacts = db.get_contact_list()
    contacts_home = app.contact.get_contact_list()
    for home_record in contacts_home:
        db_record = list(filter(lambda x: x.id == home_record.id, contacts))[0]
        assert str(db_record.fname).strip() == str(home_record.fname).strip()
        assert str(db_record.lname).strip() == str(home_record.lname).strip()
        #home_record.all_emails = "None\nNone\nNone" if home_record.all_emails == None else home_record.all_emails
        assert db_record.all_emails == home_record.all_emails
        #home_record.all_phones = "None\nNone\nNone\nNone" if home_record.all_phones == None else home_record.all_phones
        assert db_record.all_phones == home_record.all_phones
