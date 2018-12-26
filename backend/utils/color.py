import re
from random import randint

import numpy as np

from backend.src.errors import InvalidHexColorInput


def generate_random_color():
    color = "#%06x" % randint(0, 0xFFFFFF)
    return color


def hex_to_gbr(hex_color):
    pattern = re.compile(r'^#?[0-9a-fA-F]{6}$')

    if not pattern.fullmatch(hex_color):
        raise InvalidHexColorInput(hex_color)

    hex_color = hex_color.lstrip('#')

    lv = len(hex_color)

    result = [int(hex_color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]
    result.reverse()

    # adding alpha channel
    result.append(255)

    return result


def replace_black_color(image, color):
    image[np.where((image == [0, 0, 0, 255]).all(axis=2))] = hex_to_gbr(color)
    return image
