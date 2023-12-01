
# Allow to cover cases such as eightwo or nineight
word_to_num = {
    "one": 'o1e',
    "two": 't2o',
    "three": 't3e',
    "four": 'f4r',
    "five": 'f5e',
    "six": 's6x',
    "seven": 's7n',
    "eight": 'e8t',
    "nine": 'n9e'
}

def sum_calibration_values(values):
    calibration_total = 0

    for value in values:
        left_pointer = 0
        right_pointer = -1
        calibration_value = ""

        while not value[left_pointer].isnumeric():
            left_pointer += 1
        calibration_value += value[left_pointer]

        while not value[right_pointer].isnumeric():
            right_pointer -= 1
        calibration_value += value[right_pointer]

        calibration_total += int(calibration_value)

    return calibration_total


def convert_input(input_values):
    converted_values = []
    for value in input_values:
        for word, number in word_to_num.items():
            value = value.replace(word, number)
        converted_values.append(value)

    return converted_values


def output_solution_part_1():
    with open('input.txt', 'r') as input_file:
        input_values = input_file.read().split('\n')

    print(sum_calibration_values(input_values))


def output_solution_part_2():
    with open('input.txt', 'r') as input_file:
        input_values = input_file.read().split('\n')

    converted_values = convert_input(input_values)

    print(sum_calibration_values(converted_values))

output_solution_part_1()
output_solution_part_2()