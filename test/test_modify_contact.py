# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test', lastname='test1'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    id = old_contacts.index(contact)
    new_contact = Contact(firstname='name_modified', lastname='lastname_modified')
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[id] = contact
    assert old_contacts == new_contacts
