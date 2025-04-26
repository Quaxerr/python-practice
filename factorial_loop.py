# This function computes the factorial of a number using a loop.

def factorial_loop(n):
    
    result = 1
    # Multiply the result using each number from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result

# Example of how its used
n = 5
print(f"Factorial of {n} is", factorial_loop(n))
