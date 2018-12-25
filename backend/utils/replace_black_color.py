import cv2 as cv
import numpy as np


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    lv = len(hex_color)

    result = [int(hex_color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]
    result.reverse()

    # adding alpha channel
    result.append(255)

    return result


def replace_black_color(image, color):
    image[np.where((image == [0, 0, 0, 255]).all(axis=2))] = hex_to_rgb(color)
    return image
