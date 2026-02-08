#dict
d={
    "name":"yamini",
    "age": 19,
    "university":"parul"
}
#create and print
print(d)
print(d["name"])
print(len(d))
print(type(d))

#method
print(d.get("name"))
print(d.items()) #full dict
print(d.keys()) # keys
print(d.values()) #values

# a=d["university"]="DDU"
# print(a)
d.update({"age": 18,"DOB":"25-10-2006"}) #update and add new
print(d)

print(d.pop("university"))
print(d)

print(d.popitem()) #last inserted vakue

del d["age"]
print(d)

print(d.clear())