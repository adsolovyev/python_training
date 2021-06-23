# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    app.contact.modify_first_contact(Contact(firstname='name_modified', byear='1988'))


def test_add_contact_short_form(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    app.contact.create(Contact(nickname='nickname_modified', aday='27'))
