from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from base64 import b64encode

from backend.config import IMG_PATH

db_url = 'localhost:5432'
db_name = 'myslak'
db_user = 'myslak'
db_password = 'postgres'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity:
    id = Column(Integer, primary_key=True)


class AppearanceBase:
    @staticmethod
    def convert_many_base64(features):
        for feature in features:
            with open(f'{IMG_PATH}/{feature.image_url}', 'rb') as image:
                feature.image_url = b64encode(image.read())

    @staticmethod
    def convert_one_base64(data):
        with open(f'{IMG_PATH}/{data.image_url}', 'rb') as image:
            data.image_url = b64encode(image.read())
