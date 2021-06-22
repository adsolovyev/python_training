from model.contact import Contact


def test_edit_1st_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname='firstname_new', middlename='middlename_new',
                                           lastname='lastname_new', nickname='nickname_new',
                                           photo='C:\\Devel\\python_training\\photo\\test_new.jpg',
                                           title='title_new', company='company_new', address='address_new',
                                           home='home_new', mobile='mobile_new', work='work_new', fax='0000_new',
                                           email='email@1_new', email2='email@2_new', email3='email@3_new',
                                           homepage='homepage_new', bday='2', bmonth='February', byear='2001',
                                           address2='address2_new', phone2='phone2_new', notes='notes_new'))
    app.session.logout()
