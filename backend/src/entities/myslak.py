from marshmallow import Schema, fields

from sqlalchemy import Column, String

from .entity import Entity, Base


class Myslak(Entity, Base):
    __tablename__ = 'myslaks'

    title = Column(String)
    description = Column(String)
    background_url = Column(String)
    head_url = Column(String)
    cloth_url = Column(String)

    def __init__(self, title, description, created_by, background_url):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        self.background_url= background_url


class MyslakSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    background_url = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
