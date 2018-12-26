class InvalidHexColorInput(Exception):

    def __init__(self, input):
        self.input = input

    def __str__(self):
        return f'Incorrect hex color input. Allowed formats: #ffffff, ffffff. Given: {self.input}'
