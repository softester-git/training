from model.group import Group
import pytest
import random
import string
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


testdata = [Group(name="", header="", footer="")] + [Group(name=random_string("name", 10), header=random_string("head", 20), footer=random_string("foot", 20))
                                                     for i in range(5)]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(Group(name=' '.join(group.name.split())))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
