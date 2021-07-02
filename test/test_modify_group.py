from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    app.group.create_if_no_groups(db)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_group = Group(name="new_name", header="new_header", footer="new_footer")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    old_groups[index] = new_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

