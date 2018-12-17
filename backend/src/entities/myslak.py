from marshmallow import Schema, fields

from sqlalchemy import Column, String

from .entity import Entity, Base


class Myslak(Entity, Base):
    __tablename__ = 'myslaks'

    name = Column(String)
    description = Column(String)
    outline_color = Column(String)
    filling_color = Column(String)
    background = Column(String)
    head = Column(String)
    cloth = Column(String)

    def __init__(self, name, description, outline_color, filling_color, background, head, cloth, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.description = description
        self.outline_color = outline_color
        self.filling_color = filling_color
        self.background = background
        self.head = head
        self.cloth = cloth


class MyslakSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    description = fields.Str()
    outline_color = fields.Str()
    filling_color = fields.Str()
    background = fields.Number()
    head = fields.Number()
    cloth = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
