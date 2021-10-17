from copy import copy, deepcopy

l1 = [1,2,3]
l2 = l1
l2[0] = 100
print(l1)

print("liste de elemente de tip valoare")
print("shallow copy")
# shallow copy
l1=[1,2,3]
l2 = l1[:]
l2[0] = 100
print(l1)

# echivalent (shallow copy)
l1=[1,2,3]
l2 = l1.copy()
l2[0] = 100
print(l1)

# echivalent (shallow copy)
l1=[1,2,3]
l2 = copy(l1)
l2[0] = 100
print(l1)

print("deep copy")
# deep copy
l1=[1,2,3]
l2 = deepcopy(l1)
l2[0] = 100
print(l1)

print("--------------------")
print("liste de elemente de tip referinta")
print("shallow copy")
# shallow copy
l1=[[1], [2,3], [4]]
l2 = l1[:]
l2[0][0] = 100
print(l1)
for i in range(len(l1)):
    print(id(l1[i]))
    print(id(l2[i]))

print("deep copy")
# deep copy
l1=[[1], [2,3], [4]]
l2 = deepcopy(l1)
l2[0][0] = 100
print(l1)
for i in range(len(l1)):
    print(id(l1[i]))
    print(id(l2[i]))

