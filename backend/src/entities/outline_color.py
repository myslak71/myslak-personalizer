from base64 import b64encode

from PIL import Image
from marshmallow import Schema, fields, pre_dump

from sqlalchemy import Column, String

from .entity import Entity, Base, AppearanceBase


class OutlineColor(Entity, Base):
    __tablename__ = 'outline_color'

    color = Column(String)
    image_url = Column(String)

    def __init__(self, color, image_url, created_by):
        Entity.__init__(self, created_by)
        self.color = color
        self.image_url = image_url


class OutlineColorSchema(Schema, AppearanceBase):
    id = fields.Number()
    color = fields.Str()
    image_url = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()



import numpy as np
import imutils
import cv2
    @pre_dump(pass_many=True)
    def convert_image_base64(self, data, many):
        img_rgb = cv2.imread('./static/img/outline.png')

        Conv_hsv_Gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        img_rgb[mask == 255] = [0, 0, 255]

        cv2.imshow("imgOriginal", img_rgb)  # show windows

        cv2.imshow("output", res)  # show windows

        cv2.imshow("mask", mask)  # show windows

        # with Image.open(f'./static/img/outline.png') as image:
        #     data.image_url = b64encode(image.tobytes())
        print(data.image_url)
        return data
