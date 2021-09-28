import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(db, app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Contact for add to group"))
    contacts = db.get_contact_list()
    if app.group.count() == 0:
        app.group.create(Group(name="group for contact"))
    groups = db.get_group_list()
    random_contact = random.choice(contacts)
    random_group = random.choice(groups)
    if db.check_relation(group=random_group, contact=random_contact):
        print("Relation already exist")
        return
    else:
        #db.add_relation(group=random_group, contact=random_contact)
        app.contact.add_relation(group=random_group, contact=random_contact)
        check = db.check_relation(group=random_group, contact=random_contact)
        assert check is True
