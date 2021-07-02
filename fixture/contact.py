from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/edit.php') and len(wd.find_elements_by_name('photo')) > 0):
            wd.find_element_by_link_text("add new").click()

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_elements_by_id("maintable")
        if not len(wd.find_elements_by_id("maintable")) > 0:
            wd.find_element_by_link_text("home").click()
            wd.find_element_by_id("maintable")

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def create_if_no_contacts(self, db):
        self.go_to_home_page()
        if len(db.get_contact_list()) == 0:
            self.create(Contact(firstname="Name"))

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(id)
        wd.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.close_alert_and_get_its_text()
        wd.find_elements_by_class_name("msgbox")
        self.contact_cache = None

    def close_alert_and_get_its_text(self):
        wd = self.app.wd
        try:
            alert = wd.switch_to_alert()
            alert_text = alert.text
            if wd.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            wd.accept_next_alert = True

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_ddl_value("bday", contact.bday)
        self.change_ddl_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_ddl_value("aday", contact.aday)
        self.change_ddl_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def change_ddl_value(self, ddl_name, value):
        wd = self.app.wd
        if value:
            wd.find_element_by_name(ddl_name).click()
            Select(wd.find_element_by_name(ddl_name)).select_by_visible_text(value)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' % id).click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.go_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        self.go_to_home_page()
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            table = wd.find_element_by_id("maintable")
            rows = table.find_elements_by_name("entry")
            for row in rows:
                ind = row.find_element_by_name("selected[]").get_attribute("value")
                cells = row.find_elements_by_tag_name("td")
                name = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=ind, firstname=name, lastname=lastname,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[id.id]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        all_emails = "\n".join(filter(lambda x: x != "" and x is not None,
                                      [email, email2, email3]))
        all_phones = "\n".join(filter(lambda x: x != "",
                                      map(lambda x: re.sub("[() -]", "", x),
                                          filter(lambda x: x is not None,
                                                 [homephone, mobilephone, workphone, secondaryphone]))))
        return Contact(id=id, firstname=first_name, lastname=last_name,
                       address=address, all_emails_from_home_page=all_emails,
                       all_phones_from_home_page=all_phones)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        secondaryphone = re.search('P: (.*)', text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_by_id(self, id):
        contact = Contact()
        wd = self.app.wd
        self.go_to_home_page()
        table = wd.find_element_by_id("maintable")
        rows = table.find_elements_by_name("entry")
        for row in rows:
            ind = row.find_element_by_name("selected[]").get_attribute("value")
            if str(ind) == str(id):
                cells = row.find_elements_by_tag_name("td")
                name = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                contact = Contact(id=id, firstname=name, lastname=lastname, address=address,
                                  all_emails_from_home_page = all_emails, all_phones_from_home_page=all_phones)
        return contact
