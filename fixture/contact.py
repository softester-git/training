from model.contact import Contact

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
        self.return_to_home()

    def return_to_home(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home")
            wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contacts_edit_page()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def open_contacts_edit_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

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

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        list_contact = []
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            contact_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            last_name = cells[1].text
            list_contact.append(Contact(id=contact_id, lastname=last_name))
        return(list_contact)
