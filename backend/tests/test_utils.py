import unittest
from ddt import ddt, unpack, data

from backend.src.errors import InvalidHexColorInput
from ..utils.color import generate_random_color, hex_to_gbr, replace_black_color


@ddt
class TestUtils(unittest.TestCase):
    def test_hex_to_gbr_black(self):
        self.assertEqual(hex_to_gbr('#000000'), [0, 0, 0, 255])

    def test_hex_to_gbr_white(self):
        self.assertEqual(hex_to_gbr('#ffffff'), [255, 255, 255, 255])

    def test_hex_to_gbr_no_hash(self):
        self.assertEqual(hex_to_gbr('ea345f'), [95, 52, 234, 255])

    @data('#53763345', '#123', '#abcd2k')
    def test_invalid_hex_color_input(self, color_input):
        with self.assertRaises(InvalidHexColorInput):
            hex_to_gbr(color_input)

