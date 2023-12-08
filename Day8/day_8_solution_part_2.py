import re
import math

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

    all_step_counts = []

    for node in network:
        if node[-1] == 'A':
            key = node
            step_count = 0

            while not key[-1] == 'Z':
                direction = instructions[step_count % len(instructions)]
                direction_value = directions_mapping[direction]
                key = network[key][direction_value]
                step_count += 1
            all_step_counts.append(step_count)

    least_common_multiple = math.lcm(*all_step_counts)

    print(least_common_multiple)


