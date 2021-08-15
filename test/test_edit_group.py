from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for edit"))
    app.group.edit_first(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))
