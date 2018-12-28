import unittest

from mock import patch

class TestMain(unittest.TestCase):
    @patch('backend.utils.color.generate_random_color')
    def test_get_outline_color(self, mocked_generate_random_color):
        mocked_generate_random_color.return_value = ''#abc123'
        # self.assertEqual()
