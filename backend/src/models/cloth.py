from marshmallow import Schema, fields, pre_dump

from sqlalchemy import Column, String

from .model import Model, Base, AppearanceBase


class Cloth(Model, Base):
    __tablename__ = 'clothes'

    name = Column(String)
    image_url = Column(String)

    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url


class ClothSchema(Schema, AppearanceBase):
    id = fields.Number()
    name = fields.Str()
    image_url = fields.Str()

    @pre_dump(pass_many=True)
    def convert_image_base64(self, data, many):
        self.convert_to_base64(*data)
        return data
