import unittest
from day_2_solution import find_games_total, find_games_power, get_blue_cubes, get_red_cubes, get_green_cubes

class TestDay2Solution(unittest.TestCase):
    def test_get_blue_cubes(self):
        test_input = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        result = get_blue_cubes(test_input)

        assert result == ['3', '6']

    def test_get_red_cubes(self):
        test_input = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        result = get_red_cubes(test_input)

        assert result == ['4', '1']

    def test_get_green_cubes(self):
        test_input = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        result = get_green_cubes(test_input)

        assert result == ['2', '2']

    def test_find_games_total(self):
        test_input = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]
        result = find_games_total(test_input)

        assert result == 8

    def test_find_games_power(self):
        test_input = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]
        result = find_games_power(test_input)

        assert result == 2286

