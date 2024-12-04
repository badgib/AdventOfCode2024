# Advent day three

import os
import re

# Read all the lines and put them in a list
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.readlines() 

# So I decided to make it in two distinct stages as it's a simple script
# no need to make it super efficient and too complicated
# First I just prepare the oneliner for the second problem so it's even simpler
# Next thing is a fun 'findall' that just goes through input and extracts variables
# Last thing is to count them all up and sum them up for display
first_problem = 0
oneline = ''
for line in lines:
    oneline += line.replace('\n', '')
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
    for match in matches:
        first_problem += int(match[0]) * int(match[1])

print(f'First problem: {first_problem}')

second_problem = 0
# Second problem is a bit more complex because it introduces a do/don't condition.
# I chose to just sub everything that's after don't with empty string to get rid of them
# It took me a hot second to figure out that I still had last don't that ended on EOL
# Adding (?:do\(\)|$) at the end of the regex fixed it all nicely
# Last steps are the same as in the first problem, just counting up the maths
subbed = re.sub(r"don't\(\).*?(?:do\(\)|$)", "", oneline)
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', subbed)
for match in matches:
    second_problem += int(match[0]) * int(match[1])

print(f'Second problem: {second_problem}')