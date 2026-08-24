# Create a tuple
my_tuple = ("Apple", "Banana", "Mango", "Orange")

# 1. Access tuples
print("1. Access tuples")
print("First item:", my_tuple[0])
print("Second item:", my_tuple[1])
print("Second item:", my_tuple[2])

# 2. Update tuples
# Tuples cannot be changed directly, so convert it to a list
print("\n2. Update tuples")
temp = list(my_tuple)
temp[1] = "Grapes"

my_tuple = tuple(temp)
print("Updated tuple:", my_tuple)
temp1 = list(my_tuple)
temp[2] = "Cherry"

my_tuple = tuple(temp)
print("Updated tuple:", my_tuple)
# 3. Unpack tuples
print("\n3. Unpack tuples")
a, b, c, d = my_tuple
print("Unpacked values:", a, b, c, d)

# 4. Loop tuples
print("\n4. Loop tuples")
print("Looping through tuple:")
for item in my_tuple:
    print(item)

# 5. Join tuples
print("\n5. Join tuples")
tuple1 = ("Red", "Green")
tuple2 = ("Blue", "Yellow")
joined_tuple = tuple1 + tuple2
print("Joined tuple:", joined_tuple)