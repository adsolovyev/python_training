# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='name', middlename='middle name', lastname='lastname', nickname='nick',
                      photo='', title='title', company='company',
                      address='address', home='home', mobile='mobile', work='work', fax='0000',
                      email='email@1', email2='email@2', email3='email@3', homepage='homepage', bday='1',
                      bmonth='January', byear='1980', aday='15', amonth='September', ayear='1936',
                      address2='address2', phone2='home2', notes='notes')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_contact_short_form(app):
#    app.contact.create(Contact(firstname='firstname', middlename='middlename', lastname='lastname',
#                               nickname='nickname', photo='', title='',
#                               company='', address='', home='', mobile='', work='', fax='', email='email@1_short',
#                               email2='', email3='', homepage='', bday='-', bmonth='-', byear='', aday='-', amonth='-',
#                               ayear='', address2='', phone2='', notes=''))
