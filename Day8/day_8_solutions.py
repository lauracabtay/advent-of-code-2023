import re
import itertools
import math

directions_mapping = {
    "L": 0,
    "R": 1
}


def parse_file(file_name):
    maps = file_name[2:]

    network = {}

    for node in maps:
        parent = node.split(' ')[0]
        left_child = re.search(r" \((.*), ", node).group(1)
        right_child = re.search(r", (.*)\)", node).group(1)

        network[parent] = [left_child, right_child]

    return network


def count_steps_part_1(file_name, network):
    instructions = file_name[0]

    directions = itertools.cycle(instructions)
    step_counter = 0

    key = 'AAA'

    for direction in directions:
        if key == 'ZZZ':
            break

        direction_value = directions_mapping[direction]
        key = network[key][direction_value]
        step_counter += 1

    return step_counter


def count_steps_part_2(file_name, network):
    instructions = file_name[0]

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

    return least_common_multiple


with open('input.txt', 'r') as input_file:
    file = input_file.read().split('\n')

network_dict = parse_file(file)
print(count_steps_part_1(file, network_dict))
print(count_steps_part_2(file, network_dict))

