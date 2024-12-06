import os
from collections import defaultdict, deque

# Load the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

# Split into rules and updates
rules_section, updates_section = lines.strip().split("\n\n")

# Extract rules
rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]

# Extract updates
updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]

# Helper function to check if an update is valid
def is_valid_update(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

# Helper function to fix an update using topological sorting
def fix_update(update, rules):
    # Create a graph of dependencies
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sort
    sorted_update = []
    queue = deque([node for node in update if in_degree[node] == 0])

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Include any remaining pages that weren't part of the graph
    return sorted_update + [page for page in update if page not in sorted_update]

# Process updates
valid_updates = []
invalid_updates = []

for update in updates:
    if is_valid_update(update, rules):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

# Compute middle pages for valid updates
middle_pages_valid = [update[len(update) // 2] for update in valid_updates]
sum_middle_valid = sum(middle_pages_valid)

# Fix invalid updates and compute their middle pages
fixed_updates = [fix_update(update, rules) for update in invalid_updates]
middle_pages_fixed = [update[len(update) // 2] for update in fixed_updates]
sum_middle_fixed = sum(middle_pages_fixed)

# Output results
print("First problem:", sum_middle_valid)
print("Second problem:", sum_middle_fixed)
