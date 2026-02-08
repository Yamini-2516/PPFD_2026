s = {1, 5, 32, 54,5, 5, 5} # SETS ARE UNORDER
print(s)
print(len(s))
print(type(s))

#read
for i in s:
    print(i, end=" ")

print(32 in s)
s.add(2)
print(s)
s2={8,9,55,6,11}
s.update(s2)
print(s)
s.remove(5) #not present rais error
print(s)
s.discard(12) #not get error
print(s)
s.pop() #remove random
print(s)