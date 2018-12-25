from random import randint


def generate_random_color():
    color = "#%06x" % randint(0, 0xFFFFFF)
    return color
