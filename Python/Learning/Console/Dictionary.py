from collections import defaultdict
from typing import List, Dict

d = {"first": 1, "second": 2}
dd = defaultdict(list)

#Get all keys
print(d.keys())

#Remove entry
del(d["first"])

print(d)

#Clear dictionary
d.clear()

print(d)