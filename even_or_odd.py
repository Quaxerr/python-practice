# This function checks if a number is even or odd.

def check_even_or_odd(number):
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example of how its used
num = 7
print(f"{num} is", check_even_or_odd(num))
