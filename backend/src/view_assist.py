import os
import cv2 as cv
from PIL import Image
from base64 import b64encode

from backend.config import IMG_PATH
from backend.src.errors import CannotOpenImageFile
from backend.src.models.background import Background
from backend.src.models.cloth import Cloth
from backend.src.models.head import Head
from backend.src.models.myslak_color import MyslakColor, MyslakColorSchema
from backend.utils.color import replace_black_color

HERE = os.path.abspath(__name__)
os.path.dirname(HERE)


def color_save_outline(myslak):
    black_outline = cv.imread(f'{IMG_PATH}/outline.png', cv.IMREAD_UNCHANGED)
    if black_outline is None:
        raise CannotOpenImageFile(f'{IMG_PATH}/outline.png')

    new_outline_image = replace_black_color(black_outline, myslak.outline_color)
    cv.imwrite(f'{IMG_PATH}/new_outline_image.png', new_outline_image, [cv.IMWRITE_PNG_COMPRESSION, 9])


def color_save_filling(myslak):
    black_filling = cv.imread(f'{IMG_PATH}/filling.png', cv.IMREAD_UNCHANGED)

    if black_filling is None:
        raise CannotOpenImageFile(f'{IMG_PATH}/filling.png')

    new_filling_image = replace_black_color(black_filling, myslak.filling_color)
    cv.imwrite(f'{IMG_PATH}/new_filling_image.png', new_filling_image, [cv.IMWRITE_PNG_COMPRESSION, 9])


def get_urls_from_db(myslak, session):
    background = session.query(Background).get(myslak.background).image_url
    cloth = session.query(Cloth).get(myslak.cloth).image_url
    head = session.query(Head).get(myslak.head).image_url

    return {
        'background': background,
        'cloth': cloth,
        'head': head}


def compose_myslak_image(myslak, session):
    color_save_outline(myslak)

    color_save_filling(myslak)

    images_names = get_urls_from_db(myslak, session)

    images_urls = (
        f'{IMG_PATH}/{images_names["background"]}',
        f'{IMG_PATH}/new_outline_image.png',
        f'{IMG_PATH}/new_filling_image.png',
        f'{IMG_PATH}/{images_names["cloth"]}',
        f'{IMG_PATH}/{images_names["head"]}',
    )

    for url in images_urls:
        current_image = Image.open(url)
        result = Image.open(f'{IMG_PATH}/result.png')
        Image.alpha_composite(result, current_image).save(f'{IMG_PATH}/result.png')


def get_changed_image_color_base64(new_color, image_url):
    black_base = cv.imread(image_url, cv.IMREAD_UNCHANGED)

    if black_base is None:
        raise CannotOpenImageFile(image_url)

    new_image = replace_black_color(black_base, new_color)
    buffer = cv.imencode('.png', new_image, [cv.IMWRITE_PNG_COMPRESSION, 9])[1]
    new_image_b64 = b64encode(buffer)

    new_image_color = MyslakColor(new_color, new_image_b64)
    new_image_color_schema = MyslakColorSchema()
    new_image_color_schema_dump = new_image_color_schema.dump(new_image_color)

    return new_image_color_schema_dump.data
