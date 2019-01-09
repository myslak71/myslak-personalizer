from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from base64 import b64encode

from backend.config import IMG_PATH, DB_NAME, DB_PASSWORD, DB_URL, DB_USER

engine = create_engine('postgres://gpyygjzbvlaand:afd717b8b69a1f7bc364eee1a018d642c5284c6dc73693fc0253d63609a33e0b@ec2-23-21-86-22.compute-1.amazonaws.com:5432/dlnsrv42ijb8v')
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
