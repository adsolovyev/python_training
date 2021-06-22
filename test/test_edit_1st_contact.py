from model.fullname import Fullname


def test_edit_1st_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Fullname(name="name_001_new", middlename="middlename_001_new", lastname="lastname_001_new"),
                       nickname="test_nickname_new", email="email@1.long_new")

    app.session.logout()
