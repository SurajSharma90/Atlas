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

#Set default value for undefined key
d = {}
d.setdefault("first", 2)
print(d["first"])

#Copy (shallow)
d1 = {"First": 1}
d2 = d1.copy() #Shallow copy! Need to use deepcopy to really make a new dict
print(d1, d2)

#fromkeys
d1 = {"First": 1, "Second": 2}
d2 = d1.fromkeys(("First", "Second"), 3)
print(d1, d2)

#items
d1 = {"First": 1, "Second": 2}
print(d1.items())

#values
d1 = {"First": 1, "Second": 2}
print(d1.values())

#update
d1 = {"First": 1, "Second": 2}
d2 = {"Third": 3, "Fourth": 4}
print(d1, d2)
d1.update(d2)
print(d1, d2)

if "Fourth" in d1:
    print("Key Fourth is in dictionary d1")

if "Fifth" not in d1:
    print("Key Fifth is NOT in dictionary d1")