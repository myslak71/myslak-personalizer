import cv2 as cv
from PIL import Image

from backend.config import IMG_PATH
from backend.src.models.background import Background
from backend.src.models.cloth import Cloth
from backend.src.models.head import Head
from backend.utils.color import replace_black_color


def compose_myslak_image(myslak, session):
    black_outline = cv.imread('./static/img/outline.png', cv.IMREAD_UNCHANGED)
    new_outline_image = replace_black_color(black_outline, myslak.outline_color)
    cv.imwrite(f'{IMG_PATH}/new_outline_image.png', new_outline_image, [cv.IMWRITE_PNG_COMPRESSION, 9])

    black_filling = cv.imread('./static/img/filling.png', cv.IMREAD_UNCHANGED)
    new_filling_image = replace_black_color(black_filling, myslak.filling_color)
    cv.imwrite(f'{IMG_PATH}/new_filling_image.png', new_filling_image, [cv.IMWRITE_PNG_COMPRESSION, 9])

    background = session.query(Background).get(myslak.background).image_url
    cloth = session.query(Cloth).get(myslak.cloth).image_url
    head = session.query(Head).get(myslak.head).image_url

    images_urls = (
        f'{IMG_PATH}/{background}',
        f'{IMG_PATH}/new_outline_image.png',
        f'{IMG_PATH}/new_filling_image.png',
        f'{IMG_PATH}/{cloth}',
        f'{IMG_PATH}/{head}'
    )

    for url in images_urls:
        current_image = Image.open(url)
        result = Image.open(f'{IMG_PATH}/result.png')
        Image.alpha_composite(result, current_image).save(f'{IMG_PATH}/result.png')
