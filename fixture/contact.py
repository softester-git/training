from model.contact import Contact
from time import sleep
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php") and not len(wd.find_elements_by_name("submit")) > 0:
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        sleep(3)
        self.return_to_home()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select by index
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        sleep(3)
        self.return_to_home()
        self.contact_cache = None

    def return_to_home(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contacts_edit_page_by_index(index)
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contacts_edit_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def open_contacts_edit_page_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contacts_view_page_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.change_field("firstname", contact.firstname)
        self.app.change_field("middlename", contact.middlename)
        self.app.change_field("lastname", contact.lastname)
        self.app.change_field("nickname", contact.nickname)
        #wd.find_element_by_name("photo").send_keys(os.path.abspath(contact.photo)) if contact.photo is not None else ""
        self.app.change_field("title", contact.title)
        self.app.change_field("company", contact.company)
        self.app.change_field("address", contact.address)
        self.app.change_field("home", contact.home)
        self.app.change_field("mobile", contact.mobile)
        self.app.change_field("work", contact.work)
        self.app.change_field("fax", contact.fax)
        self.app.change_field("email", contact.email)
        self.app.change_field("email2", contact.email2)
        self.app.change_field("email3", contact.email3)
        self.app.change_field("homepage", contact.homepage)
        self.app.change_field_select("bday", contact.bday)
        self.app.change_field_select("bmonth", contact.bmonth)
        self.app.change_field("byear", contact.byear)
        self.app.change_field_select("aday", contact.aday)
        self.app.change_field_select("amonth", contact.amonth)
        self.app.change_field("ayear", contact.ayear)
        self.app.change_field("address2", contact.address2)
        self.app.change_field("phone2", contact.phone2)
        self.app.change_field("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                contact_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                all_phones = cells[5].text if cells[5].text != "" else None
                self.contact_cache.append(
                    Contact(id=contact_id, lastname=last_name, firstname=first_name, all_phones_from_home=all_phones))
        return(list(self.contact_cache))

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.return_to_home()
        self.open_contacts_edit_page_by_index(index)
        firstname_value = wd.find_element_by_name("firstname").get_attribute("value")
        lastname_value = wd.find_element_by_name("lastname").get_attribute("value")
        address_value = wd.find_element_by_name("address").get_attribute("value")
        id_value = wd.find_element_by_name("id").get_attribute("value")
        email_value = wd.find_element_by_name("email").get_attribute("value")
        email2_value = wd.find_element_by_name("email2").get_attribute("value")
        email3_value = wd.find_element_by_name("email3").get_attribute("value")
        homephone_value = wd.find_element_by_name("home").get_attribute("value")
        workphone_value = wd.find_element_by_name("work").get_attribute("value")
        mobilephone_value = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone_value = wd.find_element_by_name("phone2").get_attribute("value")
        return(Contact(firstname=firstname_value if firstname_value != "" else None,
                       lastname=lastname_value if lastname_value != "" else None,
                       id=id_value if id_value != "" else None,
                       address=address_value if address_value != "" else None,
                       home=homephone_value if homephone_value != "" else None,
                       work=workphone_value if workphone_value != "" else None,
                       mobile=mobilephone_value if mobilephone_value != "" else None,
                       phone2=secondaryphone_value if secondaryphone_value != "" else None
                       ))

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.return_to_home()
        self.open_contacts_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        try:
            home = re.search("H: (.*)", text).group(1)
        except:
            home = None
        try:
            work = re.search("W: (.*)", text).group(1)
        except:
            work = None
        try:
            mobile = re.search("M: (.*)", text).group(1)
        except:
            mobile = None
        try:
            phone2 = re.search("P: (.*)", text).group(1)
        except:
            phone2 = None
        return(Contact(home=home, work=work, mobile=mobile, phone2=phone2))
