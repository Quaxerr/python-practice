# This function calculates the sum of the digits of a number.

def sum_of_digits(n):
    # Initialize sum to 0
    total = 0
    #  carry out a loop until all digits are processed
    while n > 0:
        digit = n % 10  # Get the last digit
        total += digit  # Add the digit to total
        n = n // 10     # Remove the last digit
    return total

# Example of how its used
number = 12345
print("Sum of digits:", sum_of_digits(number))
