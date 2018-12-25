from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from base64 import b64encode

from backend.config import IMG_PATH, DB_NAME, DB_PASSWORD, DB_URL, DB_USER

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_URL}/{DB_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Model:
    id = Column(Integer, primary_key=True)


class AppearanceBase:
    @staticmethod
    def convert_to_base64(*features):
        for feature in features:
            with open(f'{IMG_PATH}/{feature.image_url}', 'rb') as image:
                feature.image_url = b64encode(image.read())
