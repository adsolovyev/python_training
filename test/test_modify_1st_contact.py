# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname='name_modified', byear='1988'))
    app.session.logout()


def test_add_contact_short_form(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(nickname='nickname_modified', aday='27'))
    app.session.logout()
