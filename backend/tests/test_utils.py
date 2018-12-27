import os
import unittest

import cv2 as cv
from ddt import ddt, data
from mock import patch

from backend.src.errors import InvalidHexColorArg, InvalidImageArg
from ..utils.color import generate_random_color, hex_to_gbr, replace_black_color

HERE = os.path.abspath(__name__)


@ddt
class TestUtils(unittest.TestCase):
    def test_hex_to_gbr_black(self):
        self.assertEqual(hex_to_gbr('#000000'), [0, 0, 0, 255])

    def test_hex_to_gbr_white(self):
        self.assertEqual(hex_to_gbr('#ffffff'), [255, 255, 255, 255])

    def test_hex_to_gbr_no_hash(self):
        self.assertEqual(hex_to_gbr('ea345f'), [95, 52, 234, 255])

    @data('#53763345', '#123', '#abcd2k')
    def test_invalid_hex_color_arg(self, color_input):
        with self.assertRaises(InvalidHexColorArg):
            hex_to_gbr(color_input)

    @patch('backend.utils.color.randint')
    def test_generate_random_color(self, mocked_randint):
        mocked_randint.return_value = 0xfa43e1
        self.assertEqual(generate_random_color(), '#fa43e1')

    def test_replace_black_color(self):
        black_base = cv.imread(f'{os.path.dirname(HERE)}/backend/tests/fixtures/base.png', cv.IMREAD_UNCHANGED)
        pattern_image = cv.imread(f'{os.path.dirname(HERE)}/backend/tests/fixtures/pattern.png', cv.IMREAD_UNCHANGED)

        self.assertEqual(replace_black_color(black_base, '#ff0000').all(), pattern_image.all())

    def test_invalid_image_arg(self):
        with self.assertRaises(InvalidImageArg):
            replace_black_color('String', '#a23ef1')



