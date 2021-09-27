import random


def test_del_contact_from_group(db, app):
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    try:
        random_contact = random.choice(contacts)
    except:
        print("No contacts")
        return
    try:
        random_group = random.choice(groups)
    except:
        print("No groups")
        return
    if db.check_relation(group=random_group, contact=random_contact):
        #db.del_relation(group=random_group, contact=random_contact)
        app.contact.del_relation(group=random_group, contact=random_contact)
        check = db.check_relation(group=random_group, contact=random_contact)
        assert check is False
    else:
        print("Relation not exist")
