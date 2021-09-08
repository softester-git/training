from model.group import Group
from fixture.group import GroupHelper
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/groups.json"
for a, o in opts:
    if a == "-n":
        n = int(o)
    elif a == "-f":
        f = o
testdata = [Group(name="", header="", footer="")] + [Group(name=GroupHelper.random_string("name", 10), header=GroupHelper.random_string("head", 20), footer=GroupHelper.random_string("foot", 20))
                                                     for i in range(n)]
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as fd:
    fd.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
