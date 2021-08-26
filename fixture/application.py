# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.select import Select
import re


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    # common
    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

    def change_field(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_select(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def merge_phones_like_on_home_page(self, cont):
        merg_phones = "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [cont.home, cont.mobile, cont.work, cont.phone2]))))
        return(merg_phones if merg_phones != "" else None)

    def clear(self, s):
        return (re.sub("[() -]", "", s))