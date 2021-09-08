from model.group import Group
from fixture.group import GroupHelper


constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


testdata = [Group(name="", header="", footer="")] + [Group(name=GroupHelper.random_string("name", 10), header=GroupHelper.random_string("head", 20), footer=GroupHelper.random_string("foot", 20))
                                                     for i in range(5)]