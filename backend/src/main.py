from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.myslak import Myslak, MyslakSchema
from .entities.head import Head, HeadSchema
from .entities.background import Background, BackgroundSchema
from .entities.cloth import Cloth, ClothSchema
from .entities.outline_color import OutlineColor, OutlineColorSchema
from .entities.filling_color import FillingColor, FillingColorSchema
from PIL import Image
from base64 import b64encode

from ..utils.replace_black_color import replace_black_color, cv
from backend.config import IMG_PATH

# creating the Flask application
app = Flask(__name__, static_url_path='')
CORS(app)

# if needed, generates database schema
Base.metadata.create_all(engine)


# ignoring OPTIONS method
@app.after_request
def after_request(response):
    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/myslak', methods=['POST'])
def download_myslak():
    print(request.data, 'siemku')
    print(request.get_json())
    posted_myslak = MyslakSchema(only=('name', 'description',
                                       'outline_color', 'filling_color',
                                       'background', 'cloth', 'head')).load(request.get_json())
    print(posted_myslak)
    print('siema')
    myslak = Myslak(**posted_myslak.data)

    session = Session()
    outline_color = myslak.outline_color
    filling_color = myslak.filling_color

    black_outline = cv.imread('./static/img/outline.png', cv.IMREAD_UNCHANGED)
    new_outline_image = replace_black_color(black_outline, outline_color)
    cv.imwrite(f'{IMG_PATH}/combine_outline.png', new_outline_image, [cv.IMWRITE_PNG_COMPRESSION, 9])
    new_outline_image = Image.open(f'{IMG_PATH}/combine_outline.png')

    black_filling = cv.imread('./static/img/filling.png', cv.IMREAD_UNCHANGED)
    new_filling_image = replace_black_color(black_filling, filling_color)
    cv.imwrite(f'{IMG_PATH}/combine_filling.png', new_filling_image, [cv.IMWRITE_PNG_COMPRESSION, 9])
    new_filling_image = Image.open(f'{IMG_PATH}/combine_filling.png')

    background = session.query(Background).get(myslak.background).image_url
    cloth = session.query(Cloth).get(myslak.cloth).image_url
    head = session.query(Head).get(myslak.head).image_url

    background_image = Image.open(f'{IMG_PATH}/{background}')
    cloth_image = Image.open(f'{IMG_PATH}/{cloth}')
    head_image = Image.open(f'{IMG_PATH}/{head}')
    result = Image.open(f'{IMG_PATH}/result.png')

    images = (background_image, new_outline_image, new_filling_image, cloth_image, head_image)

    for image in images:
        result = Image.open(f'{IMG_PATH}/result.png')
        Image.alpha_composite(result, image).save(f'{IMG_PATH}/result.png')

    new_myslak = MyslakSchema().dump(myslak).data
    session.close()

    # return send_file(f'{IMG_PATH}/result.png', as_attachment=True)
    return send_from_directory(f'{IMG_PATH}/', 'result.png', as_attachment=True)
    # return jsonify(new_myslak), 201

@app.route('/heads', methods=['GET'])
def get_heads():
    session = Session()
    head_objects = session.query(Head).all()

    schema = HeadSchema(many=True)
    heads = schema.dump(head_objects)

    session.close()
    return jsonify(heads.data)


@app.route('/backgrounds', methods=['GET'])
def get_backgrounds():
    session = Session()
    background_objects = session.query(Background).all()

    schema = BackgroundSchema(many=True)
    backgrounds = schema.dump(background_objects)

    session.close()
    return jsonify(backgrounds.data)


@app.route('/clothes', methods=['GET'])
def get_clothes():
    session = Session()
    cloth_objects = session.query(Cloth).all()

    schema = ClothSchema(many=True)
    clothes = schema.dump(cloth_objects)

    session.close()
    return jsonify(clothes.data)


@app.route('/outline_color', methods=['POST'])
def update_outline_color():
    print(request.get_json())
    new_color = request.get_json().get('color')
    black_outline = cv.imread('./static/img/outline.png', cv.IMREAD_UNCHANGED)

    new_outline_image = replace_black_color(black_outline, new_color)
    cv.imwrite('./static/img/output.png', new_outline_image, [cv.IMWRITE_PNG_COMPRESSION, 9])

    with open('./static/img/output.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())

    new_outline_color = OutlineColor(new_color, new_outline_b64)
    new_outline_color_schema = OutlineColorSchema()
    new_outline_color_dump = new_outline_color_schema.dump(new_outline_color)

    return jsonify(new_outline_color_dump.data)


@app.route('/outline_color', methods=['GET'])
def get_outline_color():
    with open(f'./static/img/outline.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())

    outline_color = OutlineColor('#000000', new_outline_b64)
    outline_color_schema = OutlineColorSchema()
    outline_color_dump = outline_color_schema.dump(outline_color)

    return jsonify(outline_color_dump.data)


@app.route('/filling_color', methods=['POST'])
def update_filling_color():
    new_color = request.get_json().get('color')
    black_filling = cv.imread('./static/img/filling.png', cv.IMREAD_UNCHANGED)

    new_filling_image = replace_black_color(black_filling, new_color)
    cv.imwrite('./static/img/filling_output.png', new_filling_image, [cv.IMWRITE_PNG_COMPRESSION, 9])

    with open(f'./static/img/filling_output.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())

    new_filling_color = FillingColor(new_color, new_outline_b64)
    new_filling_color_schema = FillingColorSchema()
    new_filling_color_dump = new_filling_color_schema.dump(new_filling_color)

    return jsonify(new_filling_color_dump.data)


@app.route('/filling_color', methods=['GET'])
def get_filling_color():
    new_color = "#f0f034"
    black_filling = cv.imread('./static/img/filling.png', cv.IMREAD_UNCHANGED)

    new_filling_image = replace_black_color(black_filling, new_color)
    cv.imwrite('./static/img/filling_output.png', new_filling_image, [cv.IMWRITE_PNG_COMPRESSION, 9])

    with open(f'./static/img/filling_output.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())

    new_filling_color = FillingColor(new_color, new_outline_b64)
    new_filling_color_schema = FillingColorSchema()
    new_filling_color_schema_dump = new_filling_color_schema.dump(new_filling_color)
    return jsonify(new_filling_color_schema_dump.data)
