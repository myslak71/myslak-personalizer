from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from backend.src.get_changed_image_color_data import get_changed_image_color_data
from backend.src.compose_myslak_image import compose_myslak_image
from .models.model import Session, engine, Base
from .models.myslak import Myslak, MyslakSchema
from .models.head import Head, HeadSchema
from .models.background import Background, BackgroundSchema
from .models.cloth import Cloth, ClothSchema

from backend.utils.color import generate_random_color

from backend.config import IMG_PATH

app = Flask(__name__, static_url_path='')
CORS(app)

Base.metadata.create_all(engine)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/myslak', methods=['POST'])
def download_myslak():
    posted_myslak = MyslakSchema(only=('name', 'description',
                                       'outline_color', 'filling_color',
                                       'background', 'cloth', 'head')).load(request.get_json())

    myslak = Myslak(**posted_myslak.data)

    session = Session()

    compose_myslak_image(myslak, session)

    session.close()
    return send_from_directory(f'{IMG_PATH}/', 'result.png', as_attachment=True)


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
    new_color = request.get_json().get('color')
    return jsonify(get_changed_image_color_data(new_color, './static/img/outline.png'))


@app.route('/outline_color', methods=['GET'])
def get_outline_color():
    new_color = generate_random_color()
    return jsonify(get_changed_image_color_data(new_color, './static/img/outline.png'))


@app.route('/filling_color', methods=['POST'])
def update_filling_color():
    new_color = request.get_json().get('color')
    return jsonify(get_changed_image_color_data(new_color, './static/img/filling.png'))


@app.route('/filling_color', methods=['GET'])
def get_filling_color():
    new_color = generate_random_color()
    return jsonify(get_changed_image_color_data(new_color, './static/img/filling.png'))
