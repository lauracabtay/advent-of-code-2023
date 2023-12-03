import unittest
from day_3_solution_part_1 import get_part_numbers as get_part_numbers_1, sum_part_numbers
from day_3_solution_part_2 import get_part_numbers as get_part_numbers_2, sum_gear_ratios


class TestDay2Solution(unittest.TestCase):
    def setUp(self):
        self.test_input = [
            ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
            ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
            ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '7', '5', '5'],
            ['.', '.', '.', '$', '.', '.', '*', '.', '.', '.'],
            ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']
        ]

    def test_get_part_numbers_part_1(self):
        result = get_part_numbers_1(self.test_input)
        assert result == [
            {'number': 467, 'has_adjacent_symbol': True},
            {'number': 35, 'has_adjacent_symbol': True},
            {'number': 633, 'has_adjacent_symbol': True},
            {'number': 617, 'has_adjacent_symbol': True},
            {'number': 592, 'has_adjacent_symbol': True},
            {'number': 755, 'has_adjacent_symbol': True},
            {'number': 664, 'has_adjacent_symbol': True},
            {'number': 598, 'has_adjacent_symbol': True}
        ]

    def test_get_part_numbers_part_2(self):
        result = get_part_numbers_2(self.test_input)
        assert result == [
            {'number': 467, 'has_adjacent_star': True, 'star_position': '(1, 3)'},
            {'number': 35, 'has_adjacent_star': True, 'star_position': '(1, 3)'},
            {'number': 617, 'has_adjacent_star': True, 'star_position': '(4, 3)'},
            {'number': 755, 'has_adjacent_star': True, 'star_position': '(8, 6)'},
            {'number': 598, 'has_adjacent_star': True, 'star_position': '(8, 6)'}
        ]

    def test_sum_part_numbers(self):
        test_gears = [
            {'number': 467, 'has_adjacent_symbol': True},
            {'number': 35, 'has_adjacent_symbol': True},
            {'number': 633, 'has_adjacent_symbol': True},
            {'number': 617, 'has_adjacent_symbol': True},
            {'number': 592, 'has_adjacent_symbol': True},
            {'number': 755, 'has_adjacent_symbol': True},
            {'number': 664, 'has_adjacent_symbol': True},
            {'number': 598, 'has_adjacent_symbol': True}
        ]
        result = sum_part_numbers(test_gears)
        assert result == 4361

    def test_sum_gear_ratios(self):
        test_gears = [
            {'number': 467, 'has_adjacent_star': True, 'star_position': '(1, 3)'},
            {'number': 35, 'has_adjacent_star': True, 'star_position': '(1, 3)'},
            {'number': 617, 'has_adjacent_star': True, 'star_position': '(4, 3)'},
            {'number': 755, 'has_adjacent_star': True, 'star_position': '(8, 6)'},
            {'number': 598, 'has_adjacent_star': True, 'star_position': '(8, 6)'}
        ]
        result = sum_gear_ratios(test_gears)
        assert result == 467835
