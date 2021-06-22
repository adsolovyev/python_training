from model.group import Group


def test_edit_1st_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="123_new", header="qwe_new", footer="qwe_new"))
    app.session.logout()
