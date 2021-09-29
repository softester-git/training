from model.group import Group
import pytest


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step("Given group list"):
        old_groups = db.get_group_list()
    with pytest.allure.step("Create group %s" % group):
        app.group.create(group)

    new_groups = db.get_group_list()
    old_groups.append(Group(name=group.name.strip()))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
