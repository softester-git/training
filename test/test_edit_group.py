from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for edit"))
    old_groups = app.group.get_group_list()
    group = Group(name="new_group_name", header="new_group_header", footer="new_group_footer")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
