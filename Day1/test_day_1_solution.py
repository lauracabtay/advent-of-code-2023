import unittest
from day_1_solution import convert_input, sum_calibration_values


class TestDay1Solution(unittest.TestCase):
    def test_sum_calibration_values(self):
        test_input = [
            '1abc2',
            'pqr3stu8vwx',
            'a1b2c3d4e5f',
            'treb7uchet'
        ]
        result = sum_calibration_values(test_input)

        assert result == 142

    def test_convert_input(self):
        test_input = [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
        ]
        result = convert_input(test_input)

        assert result == [
            't2o1n9e',
            'e8t2ot3e',
            'abco1e2t3exyz',
            'xt2o1e3f4r',
            '4n9ee8ts7n2',
            'zo1e8t234',
            '7pqrsts6xteen',
        ]


