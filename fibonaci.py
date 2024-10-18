# Simple Fibonacci sequence using recursion

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Input: Number of terms in the Fibonacci sequence
n = 45
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
