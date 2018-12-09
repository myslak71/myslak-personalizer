from marshmallow import Schema, fields, pre_dump

from sqlalchemy import Column, String

from .entity import Entity, Base


class Head(Entity, Base):
    __tablename__ = 'heads'

    name = Column(String)
    image_url = Column(String)

    def __init__(self, name, image_url, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.image_url = image_url


class HeadSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    image = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()

    @pre_dump(pass_many=True)
    def test(self, data, lego):
        print("to ja!: ", data)
        print(lego)
        return data





