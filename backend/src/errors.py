class InvalidHexColorArg(Exception):
    def __init__(self, color_input):
        self.input = color_input

    def __str__(self):
        return f'Incorrect hex color input. Allowed formats: #ffffff, ffffff. Given: {self.input}'


class InvalidImageArg(Exception):
    def __init__(self, image):
        self.image = image

    def __str__(self):
        return f'Incorrect image input. Expected type: numpy.ndarray. Given: {type(self.image)}'
