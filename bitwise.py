# Define two integers
a = False  # 110 in binary
b = False  # 011 in binary

# Bitwise AND
and_result = a & b  # 010 (which is 2 in decimal)

# Bitwise OR
or_result = a | b  # 111 (which is 7 in decimal)

# Bitwise XOR
xor_result = a ^ b  # 101 (which is 5 in decimal)

# Bitwise NOT for 'a'
not_result = ~a  # Inverts to 001, which is -7 in decimal

# Bitwise Left Shift
left_shift_result = a << 1  # 1100 (which is 12 in decimal)

# Bitwise Right Shift
right_shift_result = a >> 1  # 11 (which is 3 in decimal)

# Print all results
print(f"Bitwise AND of {a} & {b} = {and_result}")
print(f"Bitwise OR of {a} | {b} = {or_result}")
print(f"Bitwise XOR of {a} ^ {b} = {xor_result}")
print(f"Bitwise NOT of {a} = {not_result}")
print(f"Bitwise Left Shift of {a} << 1 = {left_shift_result}")
print(f"Bitwise Right Shift of {a} >> 1 = {right_shift_result}")
