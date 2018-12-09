from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.myslak import Myslak, MyslakSchema
from .entities.head import Head, HeadSchema

from ..config import HEAD_PATH
# creating the Flask application

app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


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
def get_backgrounds():
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

    file = open(f"{HEAD_PATH}/indian.png", 'r')
    print(head_object)
    file.close()
    # transforming into JSON-serializable objects
    schema = HeadSchema()
    print(schema)
    heads = schema.dump(head_object)

    # serializing as JSON
    session.close()
    return jsonify(heads.data)
