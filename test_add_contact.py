# -*- coding: utf-8 -*-
import pytest
from fullname import Fullname
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Fullname(name="name_001", middlename="middlename_001", lastname="lastname_001"), nickname="test_nickname", email="email@1.long")
    app.logout()


def test_add_contact_short_form(app):
    app.login(username="admin", password="secret")
    app.add_contact(Fullname(name="name_002", middlename="middlename_002", lastname="lastname_002"), nickname="test_short_nickname", email="email@1.short")
    app.logout()
