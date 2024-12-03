# Advent day two

import os

# Init a list for the numbers, one list per line, converted to integers from strings
nums = []

# Read all the lines and put them in a list
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
    lines = file.readlines() 

# Do the splitting and conversion to integers
for line in lines:
    numbers = line.split()
    nintl = []
    for n in numbers:
        nint = int(n)
        nintl.append(nint)
    nums.append(nintl)

# The function to check if a line satisfies the rule for task one    
def is_valid_line(line):

    # Determine direction of the sequence
    is_increasing = None
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]

        # Check ±1 to ±3 condition
        if not (1 <= abs(diff) <= 3):
            return False
        
        # Make sure it's not changing direction
        if is_increasing is None:
            is_increasing = diff > 0
        elif is_increasing != (diff > 0):
            return False
    return True

# Count valid lines
valid_line_count = sum(1 for line in nums if is_valid_line(line))

# Output the result of first task
print(f"Task one: {valid_line_count}")

# Function to check if a line can be made valid by removing one element
def can_be_valid_with_one_removal(line):

    # Try removing each element and check if the remaining list is valid
    for i in range(len(line)):

        # Remove the ith element
        modified_line = line[:i] + line[i+1:]
        if is_valid_line(modified_line):
            return True
    return False

# Count valid lines (including those that can be fixed by removing one element)
new_valid_line_count = 0
for line in nums:
    if is_valid_line(line) or can_be_valid_with_one_removal(line):
        new_valid_line_count += 1

# Output the result
print(f"Task two: {new_valid_line_count}")
