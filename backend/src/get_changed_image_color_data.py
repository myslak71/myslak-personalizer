import cv2 as cv

from base64 import b64encode

from backend.src.models.myslak_color import MyslakColor, MyslakColorSchema
from backend.utils.color import replace_black_color


def get_changed_image_color_base64(new_color, image_url):
    black_base = cv.imread(image_url, cv.IMREAD_UNCHANGED)

    new_image = replace_black_color(black_base, new_color)
    buffer = cv.imencode('.png', new_image, [cv.IMWRITE_PNG_COMPRESSION, 9])[1]
    new_image_b64 = b64encode(buffer)

    new_image_color = MyslakColor(new_color, new_image_b64)
    new_image_color_schema = MyslakColorSchema()
    new_image_color_schema_dump = new_image_color_schema.dump(new_image_color)

    return new_image_color_schema_dump.data
