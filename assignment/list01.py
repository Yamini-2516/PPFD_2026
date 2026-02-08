l1 = [1, 34,62, 2, 6, 11]
print(l1)
#add
l1.append(25)
print(l1)

#change
l1[2]=26
print(l1)

l1.sort()
print(l1)
l1.reverse()
print(l1)
#insert
l1.insert(2, 333333) # Insert 333333 such that its index in the list is 2
print(l1)
#delete
value = l1.pop(3) #pop value at index 3
print(value)
print(l1)