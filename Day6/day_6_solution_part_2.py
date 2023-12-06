def find_record_breaking_times(file_name):
    race_time = int(''.join(map(str, [int(x) for x in file_name[0] if x.isdigit()])))
    record_time = int(''.join(map(str, [int(x) for x in file_name[1] if x.isdigit()])))

    first_winning_time = 0
    last_winning_time = 0

    for i in range(1, race_time):
        distance = (race_time - i) * i
        if distance > record_time:
            first_winning_time = i
            break

    for j in range(race_time, 0, -1):
        distance = (race_time - j) * j
        if distance > record_time:
            last_winning_time = j
            break

    return last_winning_time - first_winning_time + 1


with open('input.txt', 'r') as input_file:
    file = input_file.read().strip().split('\n')

print(find_record_breaking_times(file))
