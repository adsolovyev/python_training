from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    app.contact.create_if_no_contacts(db)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_contact = Contact(firstname="changed_name", lastname="changed_lastname", homephone="123", mobilephone="123")
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
