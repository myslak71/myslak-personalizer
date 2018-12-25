from marshmallow import Schema, fields

from sqlalchemy import Column, String

from .model import Model, Base, AppearanceBase


class MyslakColor(Model, Base):
    __tablename__ = 'filling_color'

    color = Column(String)
    image_url = Column(String)

    def __init__(self, color, image_url):
        self.color = color
        self.image_url = image_url


class MyslakColorSchema(Schema, AppearanceBase):
    id = fields.Number()
    color = fields.Str()
    image_url = fields.Str()
