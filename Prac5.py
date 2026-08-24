# Create a dictionary
Emp = {
    "name": "Purva",
    "age": 21,
    "course": "Master of Computer Application"
}

# 1. Access dictionary items
print("1. Access dictionary items")
print("Name:", Emp["name"])
print("Age:", Emp["age"])

# 2. Change dictionary items
print("\n2. Change dictionary items")
Emp["age"] = 22
print("After changing age:",Emp)

# 3. Add dictionary items
print("\n3. Add dictionary itemss")
Emp["city"] = "Pune"
print("After adding city:", Emp)

# 4. Remove dictionary items
print("\n4. Remove dictionary items")
Emp.pop("city")
print("After removing city:", Emp)

# 5. Loop through dictionary
print("\n5. Loop through dictionary")
print("Dictionary items:")
for key, value in Emp.items():
    print(key, ":", value)

# 6. Copy dictionary
print("\n6. Copy dictionary")
Emp_copy = Emp.copy()
print("Copied dictionary:", Emp_copy)

# 7. Nested dictionary
print("\n7. Nested dictionary")
Emp = {
    "Emp1": {
        "name": "Purva",
        "age": 22
    },
    "Emp2": {
        "name": "Siddhi",
        "age": 21
    }
}

print("Nested dictionary:")
print(Emp)

# Access nested dictionary item
print("Emp 1 name:", Emp["Emp1"]["name"])