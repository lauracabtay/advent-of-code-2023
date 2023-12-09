import itertools
import operator


def get_next_last_elements(sequence):
    if set(sequence) == {0}:
        return []

    new_sequence = list(itertools.starmap(operator.sub, zip(sequence[1:], sequence)))
    return [new_sequence[-1]] + get_next_last_elements(new_sequence)


def sum_extrapolation(sequences):
    answer = 0
    for sequence in sequences:
        result = get_next_last_elements(sequence)
        answer += sum(result) + sequence[-1]

    return answer


# Part 1
with open('input.txt', 'r') as input_file:
    line = input_file.read().split('\n')
    all_sequences_part_1 = [list(map(int, element.split())) for element in line]


# Part 2
with open('input.txt', 'r') as input_file:
    line = input_file.read().split('\n')
    all_sequences_part_2 = [list(map(int, element.split()))[::-1] for element in line]

print(sum_extrapolation(all_sequences_part_1))
print(sum_extrapolation(all_sequences_part_2))
