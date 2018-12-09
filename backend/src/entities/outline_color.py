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

    @pre_dump(pass_many=True)
    def convert_image_base64(self, data, many):
        if many:
            self.convert_many_base64(data)

        else:
            self.convert_one_base64(data)

        return data
