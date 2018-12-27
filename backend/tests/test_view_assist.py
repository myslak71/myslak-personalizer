import unittest

from mock import patch

from backend.src.errors import CannotOpenImageFile
from backend.src.models.model import Session
from backend.src.models.myslak import Myslak
from backend.src.view_assist import color_save_outline, get_urls_from_db, get_changed_image_color_base64


class TestViewsSupport(unittest.TestCase):
    @patch('backend.src.view_assist.cv.imread')
    def test_color_save_outline(self, mocked_imread):
        mocked_imread.return_value = None
        myslak = Myslak('', '', '', '', '', '', '')
        with self.assertRaises(CannotOpenImageFile):
            color_save_outline(myslak)

    @patch('backend.src.view_assist.cv.imread')
    def test_color_save_filling(self, mocked_imread):
        mocked_imread.return_value = None
        myslak = Myslak('', '', '', '', '', '', '')
        with self.assertRaises(CannotOpenImageFile):
            color_save_outline(myslak)


    def test_get_changed_image_color_base64(self):
        with self.assertRaises(CannotOpenImageFile):
            get_changed_image_color_base64('#fffeee', 'invalid_url')


