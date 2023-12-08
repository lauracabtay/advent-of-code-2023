import re
import itertools

directions_mapping = {
    "L": 0,
    "R": 1
}

with open('input.txt', 'r') as input_file:
    file = input_file.read().split('\n')
    instructions = file[0]
    maps = file[2:]

    network = {}

    for node in maps:
        parent = node.split(' ')[0]
        left_child = re.search(r" \((.*), ", node).group(1)
        right_child = re.search(r", (.*)\)", node).group(1)

        network[parent] = [left_child, right_child]

    directions = itertools.cycle(instructions)
    step_counter = 0

    key = 'AAA'

    for direction in directions:
        if key == 'ZZZ':
            break

        direction_value = directions_mapping[direction]
        key = network[key][direction_value]
        step_counter += 1

    print(step_counter)
