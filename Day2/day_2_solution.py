import re


def get_blue_cubes(game_input):
    blue_matches = re.split(' blue', game_input)
    blue_matches = [blue_match.split(" ", )[-1] for blue_match in blue_matches]

    if not blue_matches[-1].isdigit():
        blue_matches.pop()

    return blue_matches


def get_red_cubes(game_input):
    red_matches = re.split(' red', game_input)
    red_matches = [red_match.split(" ", )[-1] for red_match in red_matches]

    if not red_matches[-1].isdigit():
        red_matches.pop()

    return red_matches


def get_green_cubes(game_input):
    green_matches = re.split(' green', game_input)
    green_matches = [green_match.split(" ", )[-1] for green_match in green_matches]

    if not green_matches[-1].isdigit():
        green_matches.pop()
    return green_matches


def find_games_total(input):
    game_total = 0

    for game in input:
        game_number = int(game.split("Game ", 1)[1].split(":")[0])

        blue_matches = get_blue_cubes(game)
        blue_matches = [int(blue_match) for blue_match in blue_matches if int(blue_match) > 14]

        red_matches = get_red_cubes(game)
        red_matches = [int(red_match) for red_match in red_matches if int(red_match) > 12]

        green_matches = get_green_cubes(game)
        green_matches = [int(green_match) for green_match in green_matches if int(green_match) > 13]

        if len(blue_matches) == 0 and len(red_matches) == 0 and len(green_matches) == 0:
            game_total += game_number

    return game_total


def find_games_power(input):
    game_powers_sum = 0

    for game in input:
        blue_matches = get_blue_cubes(game)
        blue_matches = [int(blue_match) for blue_match in blue_matches]
        min_blue = max(blue_matches) if blue_matches else 1

        red_matches = get_red_cubes(game)
        red_matches = [int(red_match) for red_match in red_matches]
        min_red = max(red_matches) if red_matches else 1

        green_matches = get_green_cubes(game)
        green_matches = [int(green_match) for green_match in green_matches]
        min_green = max(green_matches) if green_matches else 1

        game_power = min_blue * min_red * min_green
        game_powers_sum += game_power
    return game_powers_sum


def output_solution_part_1():
    with open('input.txt', 'r') as input_file:
        games = input_file.read().split('\n')

    print(find_games_total(games))


def output_solution_part_2():
    with open('input.txt', 'r') as input_file:
        games = input_file.read().split('\n')

    print(find_games_power(games))

output_solution_part_1()
output_solution_part_2()