# Advent day one

file_path = 'input.txt'

# Init the two variables we're interested in for the two tasks at hand
sumcounts = 0
sumdiff = 0

# Read all the lines and put them in a list
with open(file_path, 'r') as file:
    lines = file.readlines()

# Separate the columns into separate lists and convert the string to int
col1, col2 = [], []
for line in lines:
    numbers = line.split()
    col1.append(int(numbers[0]))
    col2.append(int(numbers[1]))

# Sort both columns for first problem
col1_sorted = sorted(col1)
col2_sorted = sorted(col2)

# Get the difference between two values in the same row and make it absolute
differences = [abs(a - b) for a, b in zip(col1_sorted, col2_sorted)]

# Count all the differences. It's the answer for problem one
for diff in differences:
    sumdiff += diff

# Problem two requires us to find how many times a value from column one appears in column two
# We just iterate column two values against each and every value of column one and check how many times it occured
counts = {num: col2.count(num) for num in col1}

# The answer then needs us to multiply the initial value from column one by the amount of occurences
for num, count in counts.items():
    sumcounts += num * count

# Display them results for both problems
print("Problem one: ", sumdiff)
print("Problem two: ", sumcounts)
