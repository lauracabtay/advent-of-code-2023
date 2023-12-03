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
                            if cell == '*':
                                dictionary["number"] = int(digit)
                                dictionary["has_adjacent_star"] = True
                                dictionary["star_position"] = f"({r}, {c})"

                    if not dictionary == {}:
                        part_numbers.append(dictionary)
                    digit = ''

    return part_numbers



def sum_gear_ratios(gears):
    sum_of_gear_ratios = 0
    gears_dictionary = {}

    for gear in gears:
        star_position = gear['star_position']
        number = gear['number']

        if star_position in gears_dictionary:
            gears_dictionary[star_position].append(number)
        else:
            gears_dictionary[star_position] = [number]

    for key, value in gears_dictionary.items():
        if len(value) == 2:
            sum_of_gear_ratios += value[0] * value[1]

    return sum_of_gear_ratios


with open('input.txt', 'r') as input_file:
    rows = input_file.read().split('\n')
    grid = [list(row) for row in rows]


part_numbers = get_part_numbers(grid)
print(sum_gear_ratios(part_numbers))