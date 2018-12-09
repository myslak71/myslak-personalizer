from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from base64 import b64encode

from abc import ABC
from backend.config import HEAD_PATH

db_url = 'localhost:5432'
db_name = 'wonderful_myslak_world'
db_user = 'postgres'
db_password = 'coderslab'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by


class AppearanceBase:
    @staticmethod
    def convert_appearance_list_base64(data):

        for head in data:
            with open(f'{HEAD_PATH}/{head.image_url}', 'rb') as image:
                head.image_url = b64encode(image.read())
