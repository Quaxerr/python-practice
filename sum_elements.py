# This function takes a list and returns the sum of all its elements.

def sum_list(numbers):
    # Initialize  sum total to 0
    total = 0
    # Loop every number in the list
    for num in numbers:
        total += num  # Add the current number to the total
    return total

# Example of how it is used
example_list = [1, 2, 3, 4, 5]
print("Sum of list:", sum_list(example_list))
