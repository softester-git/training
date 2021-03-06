from model.group import Group
from random import randrange


def test_edit_group_by_index(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for edit"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new_group_name", header="new_group_header", footer="new_group_footer")
    group.id = old_groups[index].id
    app.group.edit_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
