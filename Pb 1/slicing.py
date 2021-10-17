l = [5, 6, 7, 8, 9]

#6
print(l[1])
#9
print(l[len(l)-1])
print(l[-1])

#slicing
# [6, 7]
print(l[1:3])
# [5, 6, 7]
print(l[:3]) #l[0:3]
# [7, 8, 9]
print(l[2:]) #l[2:5]

print("slicing cu pas")
# [6, 8]
print(l[1:4:2])
print(l[4:1:-1])
# [9, 8, 7]

print("range")
print(list(range(1,4)))