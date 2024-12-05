# Advent day four

import os

# Read all the lines into a list
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.readlines() 

# Put the lines into a list
listed_lines = list(lines)

def count_xmas_occurrences(matrix):
    word = "XMAS"
    word_length = len(word)
    rows = len(matrix)
    cols = len(matrix[0][:-1])
    xmas_count = 0
    mas_x_count = 0

    # Define the 8 possible directions (row_delta, col_delta)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-right
        (-1, -1), # Up-left
        (1, -1),  # Down-left
        (-1, 1),  # Up-right
    ]

    # Helper function to check if "XMAS" exists starting at (row, col) in a given direction
    def check_xmas(row, col, row_delta, col_delta):
        for i in range(word_length):
            r, c = row + i * row_delta, col + i * col_delta
            if not (0 <= r < rows and 0 <= c < cols) or matrix[r][c] != word[i]:
                return False
        return True

    # Helper function to check for X "MAS"
    def check_mas_x(row, col):

        # Check if there's room for a full X
        if not (0 < row < rows - 1 and 0 < col < cols - 1):
            return False

        # Diagonal positions
        top_left = matrix[row - 1][col - 1]
        top_right = matrix[row - 1][col + 1]
        bottom_left = matrix[row + 1][col - 1]
        bottom_right = matrix[row + 1][col + 1]

        # Check all valid rotations of M and S
        diagonal_combinations = [
            (top_left, bottom_right, top_right, bottom_left),
            (top_right, bottom_left, bottom_right, top_left),
            (bottom_right, top_left, bottom_left, top_right),
            (bottom_left, top_right, top_left, bottom_right),
        ]

        for diag1, diag2, opp1, opp2 in diagonal_combinations:
            if diag1 == "M" and diag2 == "S" and opp1 == "M" and opp2 == "S":
                return True

        return False

    # Iterate through each cell in the matrix to figure both solutions
    for row in range(rows):
        for col in range(cols):

            # Search for "XMAS"
            if matrix[row][col] == "X":  # Start only if we see 'X'
                for row_delta, col_delta in directions:
                    if check_xmas(row, col, row_delta, col_delta):
                        xmas_count += 1
            # Search for X "MAS"
            if matrix[row][col] == "A":  # Start only if we see 'A'
                if check_mas_x(row, col):
                    mas_x_count += 1

    return xmas_count, mas_x_count

xmas_hits, mas_x_hits = count_xmas_occurrences(listed_lines)
print(f"First problem: {xmas_hits}")
print(f"Second problem: {mas_x_hits}")