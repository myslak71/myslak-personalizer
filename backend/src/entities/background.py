from marshmallow import Schema, fields, pre_dump

from sqlalchemy import Column, String

from .entity import Entity, Base, AppearanceBase


class Background(Entity, Base):
    __tablename__ = 'backgrounds'

    name = Column(String)
    image_url = Column(String)

    def __init__(self, name, image_url, created_by):
        self.name = name
        self.image_url = image_url


class BackgroundSchema(Schema, AppearanceBase):
    id = fields.Number()
    name = fields.Str()
    image_url = fields.Str()

    @pre_dump(pass_many=True)
    def convert_image_base64(self, data, many):
        if many:
            self.convert_many_base64(data)
        else:
            self.convert_one_base64(data)

        return data
