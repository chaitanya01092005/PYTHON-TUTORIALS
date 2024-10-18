# Dictionary Operations in Python

# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

print("Original Dictionary:", my_dict)

# 1. Accessing a value by key
print("\n1. Accessing 'name':", my_dict['name'])

# 2. Adding a new key-value pair
my_dict['email'] = 'john@example.com'
print("\n2. Dictionary after adding 'email':", my_dict)

# 3. Updating an existing key's value
my_dict['age'] = 26
print("\n3. Dictionary after updating 'age':", my_dict)

# 4. Removing a key-value pair using pop()
removed_value = my_dict.pop('city')
print("\n4. Dictionary after removing 'city':", my_dict)
print("Removed value:", removed_value)

# 5. Getting a value using get()
age = my_dict.get('age', 'Not found')
print("\n5. Getting 'age' with get():", age)

# 6. Checking if a key exists in the dictionary
has_name = 'name' in my_dict
print("\n6. Is 'name' in the dictionary?", has_name)

# 7. Iterating over keys and values
print("\n7. Iterating over dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 8. Getting all keys
keys = my_dict.keys()
print("\n8. All keys:", keys)

# 9. Getting all values
values = my_dict.values()
print("All values:", values)

# 10. Merging two dictionaries using update()
another_dict = {'gender': 'Male', 'profession': 'Engineer'}
my_dict.update(another_dict)
print("\n10. Dictionary after merging with another_dict:", my_dict)

# 11. Clearing the dictionary
my_dict.clear()
print("\n11. Dictionary after clearing:", my_dict)
