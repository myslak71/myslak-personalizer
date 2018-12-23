from base64 import b64encode

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.myslak import Myslak, MyslakSchema
from .entities.head import Head, HeadSchema
from .entities.background import Background, BackgroundSchema
from .entities.cloth import Cloth, ClothSchema
from .entities.outline_color import OutlineColor, OutlineColorSchema
from .entities.filling_color import FillingColor, FillingColorSchema
from .auth import AuthError, requires_auth
from PIL import Image

from ..utils.replace_black_color import replace_black_color, cv, np
from backend.config import IMG_PATH

# creating the Flask application

app = Flask(__name__, static_url_path='')
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


# ignores OPTIONS method
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/myslaks')
@requires_auth
def get_myslaks():
    # fetching from the database
    session = Session()
    myslak_objects = session.query(Myslak).all()

    # transforming into JSON-serializable objects
    schema = MyslakSchema(many=True)
    myslaks = schema.dump(myslak_objects)

    # serializing as JSON
    session.close()
    return jsonify(myslaks.data)


@requires_auth
@app.route('/myslaks', methods=['POST'])
def add_myslak():

    posted_myslak = MyslakSchema(only=('name', 'description',
                                       'outline_color', 'filling_color',
                                       'background', 'cloth', 'head')).load(request.get_json())
    myslak = Myslak(**posted_myslak.data, created_by="HTTP post request")

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
    print('wypelnienie', new_filling_image)

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
    print('siemmaaa2')

    return send_file(f'{IMG_PATH}/result.png', as_attachment=True)
    # return jsonify(new_myslak), 201


@requires_auth
@app.route('/myslak/1', methods=['GET'])
def show_myslak():
    session = Session()
    myslak_object = session.query(Myslak).get(4)
    print(myslak_object)

    # transforming into JSON-serializable objects
    schema = MyslakSchema()
    myslak = schema.dump(myslak_object)

    # serializing as JSON
    session.close()

    return jsonify(myslak.data)


@requires_auth
@app.route('/heads', methods=['GET'])
def get_heads():
    # fetching from the database
    session = Session()
    head_objects = session.query(Head).all()

    # transforming into JSON-serializable objects
    schema = HeadSchema(many=True)
    heads = schema.dump(head_objects)

    # serializing as JSON
    session.close()
    return jsonify(heads.data)


@requires_auth
@app.route('/heads/<int:head_id>')
def get_head(head_id):
    session = Session()
    head_object = session.query(Head).get(head_id)

    # transforming into JSON-serializable objects
    schema = HeadSchema()
    head = schema.dump(head_object)

    # serializing as JSON
    session.close()
    return jsonify(head.data)


@requires_auth
@app.route('/backgrounds', methods=['GET'])
def get_backgrounds():
    # fetching from the database
    session = Session()
    background_objects = session.query(Background).all()

    # transforming into JSON-serializable objects
    schema = BackgroundSchema(many=True)
    backgrounds = schema.dump(background_objects)

    # serializing as JSON
    session.close()
    return jsonify(backgrounds.data)


@requires_auth
@app.route('/backgrounds/<int:background_id>')
def get_background(background_id):
    session = Session()
    background_object = session.query(Background).get(background_id)

    # transforming into JSON-serializable objects
    schema = BackgroundSchema()
    background = schema.dump(background_object)

    # serializing as JSON
    session.close()
    return jsonify(background.data)


@requires_auth
@app.route('/clothes', methods=['GET'])
def get_clothes():
    # fetching from the database
    session = Session()
    cloth_objects = session.query(Cloth).all()

    # transforming into JSON-serializable objects
    schema = ClothSchema(many=True)
    clothes = schema.dump(cloth_objects)

    # serializing as JSON
    session.close()
    return jsonify(clothes.data)


@requires_auth
@app.route('/clothes/<int:cloth_id>')
def get_cloth(cloth_id):
    session = Session()
    cloth_object = session.query(Cloth).get(cloth_id)

    # transforming into JSON-serializable objects
    schema = ClothSchema()
    cloth = schema.dump(cloth_object)

    # serializing as JSON
    session.close()
    return jsonify(cloth.data)


@requires_auth
@app.route('/outline_color', methods=['POST'])
def update_outline_color():
    new_color = request.get_json().get('color')
    black_outline = cv.imread('./static/img/outline.png', cv.IMREAD_UNCHANGED)

    from base64 import b64encode
    # TODO gotta fix that, move it to the class

    new_outline_image = replace_black_color(black_outline, new_color)
    cv.imwrite('./static/img/output.png', new_outline_image, [cv.IMWRITE_PNG_COMPRESSION, 9])

    with open(f'./static/img/output.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())
    new = OutlineColor(new_color, new_outline_b64, "kibel")
    schema = OutlineColorSchema()
    cos = schema.dump(new)
    return jsonify(cos.data)


@requires_auth
@app.route('/outline_color', methods=['GET'])
def get_outline_color():
    with open(f'./static/img/outline.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())
    new = OutlineColor('#000000', new_outline_b64, "kibel")
    schema = OutlineColorSchema()
    cos = schema.dump(new)
    return jsonify(cos.data)


@requires_auth
@app.route('/filling_color', methods=['POST'])
def update_filling_color():
    new_color = request.get_json().get('color')
    black_filling = cv.imread('./static/img/filling.png', cv.IMREAD_UNCHANGED)

    from base64 import b64encode
    # TODO gotta fix that, move it to the class

    new_filling_image = replace_black_color(black_filling, new_color)
    cv.imwrite('./static/img/filling_output.png', new_filling_image, [cv.IMWRITE_PNG_COMPRESSION, 9])

    with open(f'./static/img/filling_output.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())
    new = FillingColor(new_color, new_outline_b64, "kibel")
    schema = FillingColorSchema()
    cos = schema.dump(new)
    return jsonify(cos.data)


@requires_auth
@app.route('/filling_color', methods=['GET'])
def get_filling_color():
    new_color = "#F0F034"
    black_filling = cv.imread('./static/img/filling.png', cv.IMREAD_UNCHANGED)

    from base64 import b64encode
    # TODO gotta fix that, move it to the class

    new_filling_image = replace_black_color(black_filling, new_color)
    cv.imwrite('./static/img/filling_output.png', new_filling_image, [cv.IMWRITE_PNG_COMPRESSION, 9])

    with open(f'./static/img/filling_output.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())
    new = FillingColor(new_color, new_outline_b64, "kibel")
    schema = FillingColorSchema()
    cos = schema.dump(new)
    return jsonify(cos.data)
