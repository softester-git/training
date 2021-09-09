from model.contact import Contact
from fixture.contact import ContactHelper
import random
import pytest


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(Contact(firstname=' '.join(contact.firstname.split()), lastname=' '.join(contact.lastname.split())))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
