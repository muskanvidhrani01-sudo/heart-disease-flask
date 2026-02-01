fruits={"apple","mango","orange","mango"}
veg={"onion","tomato","orange","potato"}
for x in fruits:
    print(x)

print(fruits.union(veg))
print(fruits.intersection(veg))
print(veg.difference(fruits))