# Example list of words
words = ['Python', 'is', 'fun']

# Join the list into a single string with spaces
joined_string = " ".join(words)
print("Joined string:", joined_string)  # Output: 'Python is fun'

# Joining with a different separator
csv_output = ",".join(words)
print("CSV output:", csv_output)  # Output: 'Python,is,fun'

# Joining with hyphens
hyphenated = "-".join(words)
print("Hyphenated:", hyphenated)  # Output: 'Python-is-fun'
