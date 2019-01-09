import os

IMG_PATH = os.path.dirname(os.path.abspath(__file__)) + "/static/img"

DB_URL = os.environ['DATABASE_URL']
DB_NAME = os.environ['DATABASE_NAME']
DB_USER = os.environ['DATABASE_USER']
DB_PASSWORD = os.environ['DATABASE_PASSWORD']

print('hassssllllllll', DB_PASSWORD)