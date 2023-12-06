def find_record_breaking_times(file_name):
    race_times = [int(x) for x in file_name[0].split() if x.isdigit()]
    record_times = [int(x) for x in file_name[1].split() if x.isdigit()]

    wins = []

    for index, race in enumerate(race_times):
        win_count = 0
        for i in range(1, race):
            distance = (race - i) * i

            if distance > record_times[index]:
                win_count += 1

        wins.append(win_count)

    result = 1

    for win in wins:
        result *= win

    return result


with open('input.txt', 'r') as input_file:
    file = input_file.read().strip().split('\n')

print(find_record_breaking_times(file))
