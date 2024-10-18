# Example of a for loop
print("For Loop:")
for i in range(5):  # Looping from 0 to 4
    print(i)  # Output: 0, 1, 2, 3, 4

# Example of a while loop
print("\nWhile Loop:")
count = 0
while count < 5:  # Continue looping as long as count is less than 5
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1  # Increment count

# Example of a nested loop
print("\nNested Loop:")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")  # Output: i and j combinations

# Example of using break in a loop
print("\nBreak Statement:")
for i in range(5):
    if i == 3:  # Break the loop when i is 3
        break
    print(i)  # Output: 0, 1, 2

# Example of using continue in a loop
print("\nContinue Statement:")
for i in range(5):
    if i == 2:  # Skip the iteration when i is 2
        continue
    print(i)  # Output: 0, 1, 3, 4

# Example of using else with a loop
print("\nElse with Loop:")
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
else:
    print("Loop completed!")  # This runs after the loop completes
