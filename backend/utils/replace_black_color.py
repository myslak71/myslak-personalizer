from PIL import Image
import numpy as np


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def replace_black_color(image, color):
    im = image.convert('RGBA')
    data = np.array(im)

    red, green, blue, alpha = data.T

    black_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][black_areas.T] = hex_to_rgb(color)  # Transpose back needed

    im2 = Image.fromarray(data)

    return im2



