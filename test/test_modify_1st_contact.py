# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test', lastname='test1'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='name_modified', lastname='lastname_modified')
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_contact_short_form(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname='test'))
#    app.contact.create(Contact(nickname='nickname_modified', aday='27'))
