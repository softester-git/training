from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for edit"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
