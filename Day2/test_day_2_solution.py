import unittest
from day_2_solution import find_games_total, find_games_power, ColourCubes


class TestColorCubes(unittest.TestCase):
    def setUp(self):
        self.color_cubes_instance = ColourCubes("blue")

    def test_get_colour_cubes(self):
        no_blue = 'Game 3: 8 green, 20 red; 4 red, 13 green; 5 green, 1 red'
        one_blue = 'Game 3: 6 blue, 20 red; 4 red, 13 green; 5 green, 1 red'
        multiple_blue = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red; 5 green'

        result = self.color_cubes_instance.get_colour_cubes(no_blue)
        assert result == []

        result = self.color_cubes_instance.get_colour_cubes(one_blue)
        assert result == [6]

        result = self.color_cubes_instance.get_colour_cubes(multiple_blue)
        assert result == [6, 5]

    def test_get_impossible_cubes(self):
        no_blue = 'Game 3: 8 green, 20 red; 4 red, 13 green; 5 green, 1 red'
        one_blue = 'Game 3: 8 green, 15 blue, 6 blue, 1 red'
        multiple_blue = 'Game 3: 8 green, 15 blue; 17 blue, 4 red; 5 blue'

        result = self.color_cubes_instance.get_impossible_cubes(no_blue, 14)
        assert result == []

        result = self.color_cubes_instance.get_impossible_cubes(one_blue, 14)
        assert result == [15]

        result = self.color_cubes_instance.get_impossible_cubes(multiple_blue, 14)
        assert result == [15, 17]


class TestDay2Solution(unittest.TestCase):
    def setUp(self):
        self.test_input = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]

    def test_find_games_total(self):
        result = find_games_total(self.test_input)
        assert result == 8

    def test_find_games_power(self):
        result = find_games_power(self.test_input)
        assert result == 2286
