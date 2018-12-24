from marshmallow import Schema, fields, pre_dump

from sqlalchemy import Column, String

from .entity import Entity, Base, AppearanceBase


class FillingColor(Entity, Base):
    __tablename__ = 'filling_color'

    color = Column(String)
    image_url = Column(String)

    def __init__(self, color, image_url):
        self.color = color
        self.image_url = image_url


class FillingColorSchema(Schema, AppearanceBase):
    id = fields.Number()
    color = fields.Str()
    image_url = fields.Str()



