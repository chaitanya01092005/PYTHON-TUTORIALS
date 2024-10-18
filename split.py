# Example string
sentence = "Python is a powerful programming language"

# Split the string into a list
words = sentence.split()
print("List of words:", words)  # Output: ['Python', 'is', 'a', 'powerful', 'programming', 'language']

# Splitting with a specific separator
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print("List of fruits:", fruits)  # Output: ['apple', 'banana', 'cherry']

# Using maxsplit
limited_split = sentence.split(" ", 3)
print("Limited split:", limited_split) 
 # Output: ['Python', 'is', 'a powerful programming language']
