# Set Operations in Python

# Creating a set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}






print("Set 1:", set1)
print("Set 2:", set2)

# 1. Union
union_set = set1.union(set2)
print("\nUnion of Set 1 and Set 2:", union_set)

# 2. Intersection
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# 3. Difference
difference_set = set1.difference(set2)
print("Difference of Set 1 and Set 2:", difference_set)

# 4. Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of Set 1 and Set 2:", symmetric_difference_set)

# 5. Adding an element to the set
set1.add(9)
print("\nSet 1 after adding 9:", set1)

# 6. Removing an element from the set
set1.remove(9)
print("Set 1 after removing 9:", set1)

# 7. Checking if a set is a subset
is_subset = {1, 2}.issubset(set1)
print("\nIs {1, 2} a subset of Set 1?", is_subset)

# 8. Checking if a set is a superset
is_superset = set1.issuperset({1, 2})
print("Is Set 1 a superset of {1, 2}?", is_superset)

# 9. Checking for disjoint sets (no common elements)
is_disjoint = set1.isdisjoint({10, 11})
print("Are Set 1 and {10, 11} disjoint sets?", is_disjoint)

# 10. Clearing a set (removing all elements)
set1.clear()
print("\nSet 1 after clearing all elements:", set1)

my_set = {1, 2, 3, 4}
print(len(my_set))  # Output: 4