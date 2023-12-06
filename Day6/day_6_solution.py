def find_record_breaking_times(file_name):
    race_times = [int(x) for x in file_name[0].split() if x.isdigit()]
    record_times = [int(x) for x in file_name[1].split() if x.isdigit()]

    wins = 1

    for index, race in enumerate(race_times):
        first_winning_time = 0
        last_winning_time = 0

        for i in range(1, race):
            distance = (race - i) * i
            if distance > record_times[index]:
                first_winning_time = i
                break

        for j in range(race, 0, -1):
            distance = (race - j) * j
            if distance > record_times[index]:
                last_winning_time = j
                break

        wins *= last_winning_time - first_winning_time + 1

    return wins


with open('input.txt', 'r') as input_file:
    file = input_file.read().strip().split('\n')

print(find_record_breaking_times(file))
