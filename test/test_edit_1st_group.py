from model.group import Group


def test_edit_1st_group(app):
    app.group.edit_first_group(Group(name="123_new", header="qwe_new", footer="qwe_new"))
