import re


class ColourCubes:
    def __init__(self, colour):
        self.colour = colour

    def get_colour_cubes(self, game_input):
        colour_sections = re.split(" " + self.colour, game_input)
        colour_matches = [
            int(colour_section.split(" ")[-1]) for colour_section in colour_sections
            if colour_section.split(" ")[-1].isdigit()
        ]
        return colour_matches

    def get_impossible_cubes(self, game_input, max_limit):
        return [
            int(colour_match) for colour_match in self.get_colour_cubes(game_input)
            if int(colour_match) > max_limit
        ]


def find_games_total(input):
    game_total = 0

    for game in input:
        game_number = int(game.split("Game ", 1)[1].split(":")[0])

        impossible_blue = ColourCubes('blue').get_impossible_cubes(game, 14)
        impossible_red = ColourCubes('red').get_impossible_cubes(game, 12)
        impossible_green = ColourCubes('green').get_impossible_cubes(game, 13)

        if len(impossible_blue) + len(impossible_red) + len(impossible_green) == 0:
            game_total += game_number

    return game_total


def find_games_power(input):
    game_powers_sum = 0

    for game in input:
        blue_cubes = ColourCubes('blue').get_colour_cubes(game)
        min_blue = max(blue_cubes) if blue_cubes else 1

        red_cubes = ColourCubes('red').get_colour_cubes(game)
        min_red = max(red_cubes) if red_cubes else 1

        green_cubes = ColourCubes('green').get_colour_cubes(game)
        min_green = max(green_cubes) if green_cubes else 1

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