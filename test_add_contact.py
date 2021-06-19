# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from fullname import Fullname
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.add_firstname_middlename_lastname(wd, Fullname(name="name_001", middlename="middlename_001", lastname="lastname_001"))
        self.add_nickname(wd, nickname="test_nickname")
        self.add_title(wd, title="test_title")
        self.add_company(wd, company="company_name")
        self.add_address(wd, address="test street, 1, 1")
        self.add_home(wd, home="home sweet home")
        self.add_mobile(wd, mobile="+0 000 000 0000")
        self.add_work(wd, work="work work work")
        self.add_fax(wd, fax="+1 111 111 1111")
        self.add_email(wd, email="email@1")
        self.add_email2(wd, email="email@2")
        self.add_email3(wd, email="email@3")
        self.add_homepage(wd, homepage="www.homepage.com")
        self.add_birthday_info(wd)
        self.add_aniversary_info(wd)
        self.add_second_address(wd, secondaryaddress="address #2")
        self.add_second_phone(wd, secondaryhome="home #2")
        self.add_notes(wd, notes="notes notes notes")
        self.submit_new_contact(wd)
        self.go_to_home_page(wd)
        self.logout(wd)

    def test_add_contact_short_form(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.add_firstname_middlename_lastname(wd, Fullname(name="name_001", middlename="middlename_001", lastname="lastname_001"))
        self.add_nickname(wd, nickname="test_nickname")
        self.add_email(wd, email="email@1")
        self.add_birthday_info(wd)
        self.submit_new_contact(wd)
        self.go_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def go_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def submit_new_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_notes(self, wd, notes):
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)

    def add_second_phone(self, wd, secondaryhome):
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(secondaryhome)

    def add_second_address(self, wd, secondaryaddress):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(secondaryaddress)

    def add_aniversary_info(self, wd):
        # add day
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[3]").click()
        # add month
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[2]").click()
        # add year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")

    def add_birthday_info(self, wd):
        # add day
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        # ad month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//option[@value='January']").click()
        # add year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2000")

    def add_homepage(self, wd, homepage):
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)

    def add_email3(self, wd, email):
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email)

    def add_email2(self, wd, email):
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email)

    def add_email(self, wd, email):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)

    def add_fax(self, wd, fax):
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)

    def add_work(self, wd, work):
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work)

    def add_mobile(self, wd, mobile):
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)

    def add_home(self, wd, home):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home)

    def add_address(self, wd, address):
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)

    def add_company(self, wd, company):
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)

    def add_title(self, wd, title):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)

    def add_nickname(self, wd, nickname):
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)

    def add_firstname_middlename_lastname(self, wd, fullname):
        # add firstname, middlename, lastname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(fullname.name)
        # add middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(fullname.middlename)
        # add lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(fullname.lastname)

    def open_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
