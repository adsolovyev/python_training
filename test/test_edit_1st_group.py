from model.group import Group


def test_edit_1st_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(name="123_new", header="qwe_new", footer="qwe_new"))
