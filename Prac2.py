fruits = ["apple", "banana", "cherry", "orange"]
list2 = [1, 2, 3]
# Access
print("Access at index 1:", fruits[1:2])
print("Access at index -1:", fruits[-1]) #negative indexing
# Change
fruits[1] = "mango"
print("After changing index 1:", fruits)
# Remove
fruits.remove("orange")
print("After removing orange:", fruits)
# Loop
print("Loop through the list:")
for x in fruits:
    print(x)

# List comprehension
newlist = [x for x in fruits if "a" in x]
print("Fruits containing 'a':", newlist)
# Sort
fruits.sort()
print("After sorting:", fruits)
#sort in decending
fruits.sort(reverse=True)
print("decending sorting:",fruits)
# append() append the elements of a list to another list
for x in list2:
  fruits.append(x)
print("joined list:",fruits)
#extend() method to add list2 at the end of list1:
fruits.extend(list2)
print(fruits)
