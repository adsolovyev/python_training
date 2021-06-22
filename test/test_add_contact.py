# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname='name', middlename='middle name', lastname='lastname', nickname='nick',
                               photo='C:\\Devel\\python_training\\photo\\test.jpg', title='title', company='company',
                               address='address', home='home', mobile='mobile', work='work', fax='0000',
                               email='email@1', email2='email@2', email3='email@3', homepage='homepage', bday='1',
                               bmonth='January', byear='1980', address2='address2', phone2='0987654321', notes='notes'))
    app.session.logout()


def test_add_contact_short_form(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname='firstname', middlename='middlename', lastname='lastname',
                               nickname='nickname', photo='', title='',
                               company='', address='', home='', mobile='', work='', fax='', email='email@1_short',
                               email2='', email3='', homepage='', bday='-', bmonth='-', byear='',
                               address2='', phone2='', notes=''))
    app.session.logout()
