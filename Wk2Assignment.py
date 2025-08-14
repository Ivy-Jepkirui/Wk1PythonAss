# Start with an empty list
my_list = []

# 1. Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 2. Insert 15 at second position (index 1)
my_list.insert(1, 15)

# 3. Extend list with [50, 60, 70]
my_list.extend([50, 60, 70])

# 4. Remove the last element
my_list.pop()


# 5. Sort the list in ascending order
my_list.sort()

# 6. Find and print the index of the value 30
index_of_30 = my_list.index(30)

print("Final my_list:", my_list)
print("Index of 30:", index_of_30)
