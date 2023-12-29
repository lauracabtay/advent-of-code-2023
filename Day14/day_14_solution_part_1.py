from collections import Counter
import re


def reverse_grid(grid):
    reversed_grid = []

    for col in range(len(grid[0])):
        new_arr = ''
        for index, value in enumerate(grid):
            new_arr += grid[index][col]

        reversed_grid.append(new_arr)
    return reversed_grid


def tilt_grid(grid):
    tilted_grid = []

    for row in grid:
        if '#' in row:
            split_row = re.split(r'(#)', row)
            tilted_row = []
            for segment in split_row:
                if 'O' in segment:
                    segment = Counter(segment)
                    segment = 'O' * segment['O'] + '.' * segment['.']
                tilted_row.append(segment)
            tilted_row = ''.join(tilted_row)
        else:
            row = Counter(row)
            tilted_row = 'O' * row['O'] + '.' * row['.']

        tilted_grid.append(''.join(tilted_row))

    return tilted_grid


def calculate_load(grid):
    counter = 0

    for line in grid:
        for index, char in enumerate(line):
            if char == 'O':
                counter += len(line) - index

    return counter


with open('input.txt', 'r') as input_file:
    input_grid = input_file.read().split('\n')

grid = reverse_grid(input_grid)
tilted_grid = tilt_grid(grid)
print(calculate_load(tilted_grid))
