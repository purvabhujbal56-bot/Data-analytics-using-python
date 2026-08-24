# Create a set
fruits = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
print("Original Set:", fruits)

# 1. Access Set Items
print("\n1. Access Set Items")
for fruit in fruits:
    print(fruit)
print("\n Check if 'banana' is in the set")
print("banana" in fruits)  #Check if "banana" is in the set

# 2. Add Set Items
print("\n2. Add Set Items")
fruits.add("orange")
print("After add:", fruits)
# Add multiple items
fruits.update(["mango", "grapes"])
print("After update:", fruits)
#Add elements of a list to a set:
fruits.update(mylist)
print("After update with list:", fruits)

# 3. Remove Set Items
print("\n3. Remove Set Items")
fruits.remove("banana")
print("After remove():", fruits)
# discard() does not give an error if item does not exist
fruits.discard("apple")
print("After discard():", fruits)

# 4. Loop Sets
print("\n4. Loop Set")
for fruit in fruits:
    print(fruit)

# 5. Join Sets
print("\n5. Join Sets")
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "mango", "banana"}
# Union - joins all items
set3 = set1.union(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Joined Set:", set3)
#intersection - returns items that are present in both sets
set4 = set1.intersection(set2)
print("Intersection Set:", set4)
#difference - returns items that are present in set1 but not in set2
set5 = set1.difference(set2)    
print("Difference Set:", set5)
