from random import randint

l = []
for i in range(0,10):
    l.append(randint(0, 100))

print(l)

#sort
l = sorted(l)

print(l)

#Two lists and zip
l1 = []
l2 = []
for i in range(0,10):
    l1.append(randint(0, 100))
    l2.append(randint(0, 100))

print(l1, l2)

for i, k in zip(l1, l2):
    print(i, k)