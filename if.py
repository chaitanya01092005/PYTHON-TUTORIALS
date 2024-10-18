# # Example 1: Simple if statement
# num = 10
# if num > 5:
#     print("Simple if: The number is greater than 5")

# # Example 2: if-else statement
# num = 3
# if num > 5:
#     print("if-else: The number is greater than 5")
# else:
#     print("if-else: The number is not greater than 5")

# # Example 3: if-elif-else statement
# num = 0
# if num < 0:
#     print("if-elif-else: The number is negative")
# elif num == 0:
#     print("if-elif-else: The number is zero")
# else:
#     print("if-elif-else: The number is positive")

# # Example 4: Nested if statement
# num = 15
# if num > 10:
#     print("Nested if: The number is greater than 10")
#     if num % 2 == 0:
#         print("Nested if: The number is even")
#     else:
#         print("Nested if: The number is odd")

# # Example 5: Ternary if (conditional expression)
# age = 18
# result = "Adult" if age >= 18 else "Minor"
# print(f"Ternary if: {result}")






# Take input for temperature in Celsius
Temp = int(input("Enter temperature in Celsius:\n"))

# Use a ternary operator to determine the status based on the temperature
Status = "Hot" if Temp > 35 else "Normal"
print(f"Status: {Status}")

# Example of nested ternary operator
Status = "Hot" if Temp > 35 else "Cold" if Temp < 20 else "Normal"
print(f"Nested Status: {Status}")
