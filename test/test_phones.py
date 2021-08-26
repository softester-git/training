def test_phones_on_edit_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home == app.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_edit_page.home == contact_from_view_page.home
    assert contact_from_edit_page.mobile == contact_from_view_page.mobile
    assert contact_from_edit_page.work == contact_from_view_page.work
    assert contact_from_edit_page.phone2 == contact_from_view_page.phone2
