# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10 + string.punctuation
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, postfix, maxlen):
    symbols = string.ascii_letters + "._-"
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


def random_phone(maxlen):
    symbols = '0123456789'
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", email='', mobilephone='')] + [
    Contact(firstname=random_string('name', 10), lastname=random_string('header', 20),
            email=random_email('email', '@gmail.com', 10), mobilephone=random_phone(10),
            email2=random_email('email', '@mail.ru', 10), title=random_string('name', 10),
            address=random_address(20))
    for i in range(5)
]

# contact = Contact(firstname='name', middlename='middle name', lastname='lastname', nickname='nick',
#                  photo='', title='title', company='company',
#                  address='address', home='home', mobile='mobile', work='work', fax='0000',
#                  email='email@1', email2='email@2', email3='email@3', homepage='homepage', bday='1',
#                  bmonth='January', byear='1980', aday='15', amonth='September', ayear='1936',
#                  address2='address2', phone2='home2', notes='notes')


@pytest.mark.parametrize('contact', testdata, ids=(repr(x) for x in testdata))
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

