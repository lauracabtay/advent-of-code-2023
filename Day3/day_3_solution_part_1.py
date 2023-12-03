def get_part_numbers(grid):
    part_numbers = []

    for row_index, row in enumerate(grid):
        digit = ''

        for col_index, col in enumerate(row):
            dictionary = {}

            if col.isdigit():
                digit += col

                if col_index == len(row) - 1 or not row[col_index + 1].isdigit():
                    row_min = row_index - 1 if row_index > 0 else 0
                    row_max = row_index + 1 if row_index < len(grid) - 1 else len(grid) - 1
                    col_min = col_index - len(digit) if col_index > 0 else 0
                    col_max = col_index + 1 if col_index < len(row) - 1 else len(row) - 1

                    for r in range(row_min, row_max + 1):
                        for c in range(col_min, col_max + 1):
                            cell = grid[r][c]
                            if not cell.isalpha() and not cell.isdigit() and not cell == '.':
                                dictionary["number"] = int(digit)
                                dictionary["has_adjacent_symbol"] = True

                    if not dictionary == {}:
                        part_numbers.append(dictionary)
                    digit = ''

    return part_numbers


def sum_part_numbers(gears):
    sum_of_part_numbers = 0
    for gear in gears:
        sum_of_part_numbers += gear["number"]

    return sum_of_part_numbers


with open('input.txt', 'r') as input_file:
    rows = input_file.read().split('\n')
    grid = [list(row) for row in rows]

part_numbers = get_part_numbers(grid)
print(sum_part_numbers(part_numbers))




