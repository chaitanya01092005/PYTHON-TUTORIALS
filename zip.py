zipped = zip([1, 2, 3], ['a', 'b', 'c'])

numbers, letters = zip(*zipped)

print(numbers)  # Output: (1, 2, 3)
print(letters)  # Output: ('a', 'b', 'c')



names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
# Output:
# Alice is 25 years old.
# Bob is 30 years old.
# Charlie is 22 years old.
