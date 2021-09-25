def test_contact_home_page_eq_edit_page(app, db):
    contacts = db.get_contact_list()
    contacts_home = app.contact.get_contact_list()
    for home_record in contacts_home:
        db_record = list(filter(lambda x: x.id == home_record.id, contacts))[0]
        assert str(db_record.firstname).strip() == str(home_record.firstname).strip()
        assert str(db_record.lastname).strip() == str(home_record.lastname).strip()
        assert str(db_record.address).strip() == str(home_record.address).strip()
        db_record.home = "+" + db_record.home[2:] if db_record.home.startswith("00") else db_record.home
        #db_record.home = "" if db_record.home == "0" else db_record.home
        db_record.mobile = "+" + db_record.mobile[2:] if db_record.mobile.startswith("00") else db_record.mobile
        #db_record.mobile = "" if db_record.mobile == "0" else db_record.mobile
        db_record.work = "+" + db_record.work[2:] if db_record.work.startswith("00") else db_record.work
        #db_record.work = "" if db_record.work == "0" else db_record.work
        db_record.phone2 = "+" + db_record.phone2[2:] if db_record.phone2.startswith("00") else db_record.phone2
        #db_record.phone2 = "" if db_record.phone2 == "0" else db_record.phone2
        #db_phones = ((db_record.home + "\n" + db_record.mobile + "\n" + db_record.work + "\n" + db_record.phone2).replace("\n\n\n","")).replace("\n\n","\n")
        #db_phones = db_phones[:-2] if db_phones.endswith("\n") else db_phones
        #db_phones = db_phones[:-1] if db_phones.endswith("\n0") else db_phones
        #home_record.all_phones_from_home = home_record.all_phones_from_home[:-1] if home_record.all_phones_from_home.endswith("\n0") else home_record.all_phones_from_home
        #home_record.all_phones_from_home = home_record.all_phones_from_home[1:] if home_record.all_phones_from_home.startswith("0\n") else home_record.all_phones_from_home
        #home_record.all_phones_from_home = home_record.all_phones_from_home[:-1] if home_record.all_phones_from_home.endswith("\n") else home_record.all_phones_from_home
        # assert db_phones == home_record.all_phones_from_home
        db_phones = str(db_record.home) + str(db_record.mobile) + str(db_record.work) + str(db_record.phone2)
        home_phones = home_record.all_phones_from_home.replace("\n","")
        assert db_phones == home_phones
        db_emails = str(db_record.email) + str(db_record.email2) + str(db_record.email3)
        home_emails = home_record.all_emails_from_home.replace("\n","")
        assert db_emails == home_emails
