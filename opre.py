# 1. Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# 2. Appending an element to the list
my_list.append(6)
print("After appending 6:", my_list)

# 3. Inserting an element at a specific position
my_list.insert(2, 10)
print("After inserting 10 at index 2:", my_list)

# 4. Removing an element by value
my_list.remove(10)
print("After removing 10:", my_list)

# 5. Popping an element (removes and returns the last element)
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After popping an element:", my_list)

# 6. Finding the index of an element
index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4)

# 7. Sorting the list
my_list.sort()
print("After sorting:", my_list)

# 8. Reversing the list
my_list.reverse()
print("After reversing:", my_list)

# 9. Counting occurrences of an element
count_of_3 = my_list.count(3)
print("Count of 3:", count_of_3)

# 10. Extending the list with another list
my_list.extend([7, 8, 9])
print("After extending with [7, 8, 9]:", my_list)
