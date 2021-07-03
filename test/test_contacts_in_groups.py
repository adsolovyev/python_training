import random
from model.group import Group
from model.contact import Contact


def test_add_and_remove_contact_in_group(app, db, orm):
    app.contact.create_if_no_contacts(db)
    app.group.create_if_no_groups(db)
    wd = app.wd
    app.contact.go_to_home_page()
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    count_contact_in_group = len(orm.get_contacts_in_group(Group(id=group.id)))
    app.contact.select_contact_by_id(contact.id)
    to_group = wd.find_element_by_name("to_group")
    to_group.find_element_by_css_selector("option[value='%s']" % group.id).click()
    wd.find_element_by_name("add").click()
    wd.find_element_by_css_selector("a[href='./?group=%s']" % group.id).click()
    assert len(orm.get_contacts_in_group(Group(id=group.id))) == count_contact_in_group + 1
    app.contact.select_contact_by_id(contact.id)
    wd.find_element_by_css_selector("input[value='Remove from \"%s\"']" % group.name).click()
    assert len(orm.get_contacts_in_group(Group(id=group.id))) == count_contact_in_group
