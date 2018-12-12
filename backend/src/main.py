from base64 import b64encode

from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.myslak import Myslak, MyslakSchema
from .entities.head import Head, HeadSchema
from .entities.background import Background, BackgroundSchema
from .entities.cloth import Cloth, ClothSchema
from .entities.outline_color import OutlineColor, OutlineColorSchema
from .entities.filling_color import FillingColor, FillingColorSchema

from ..utils.replace_black_color import replace_black_color, cv, np
from PIL import Image

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


@app.route('/myslaks', methods=['POST'])
def add_myslak():
    # mount exam object
    posted_myslak = MyslakSchema(only=('title', 'description', 'background_url')).load(request.get_json())
    myslak = Myslak(**posted_myslak.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(myslak)
    session.commit()

    # return created exam
    new_myslak = MyslakSchema().dump(myslak).data
    session.close()
    return jsonify(new_myslak), 201


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


@app.route('/outline_color', methods=['GET'])
def get_outline_color():
    with open(f'./static/img/outline.png', 'rb') as image:
        new_outline_b64 = b64encode(image.read())
    new = OutlineColor('#000000', new_outline_b64, "kibel")
    schema = OutlineColorSchema()
    cos = schema.dump(new)
    return jsonify(cos.data)

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