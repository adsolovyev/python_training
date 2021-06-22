# -*- coding: utf-8 -*-

from model.fullname import Fullname


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Fullname(name="name_001", middlename="middlename_001", lastname="lastname_001"),
                       nickname="test_nickname", email="email@1.long")
    app.session.logout()


def test_add_contact_short_form(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Fullname(name="name_002", middlename="middlename_002", lastname="lastname_002"),
                       nickname="test_short_nickname", email="email@1.short")
    app.session.logout()
