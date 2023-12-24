import base64

from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS, cross_origin
from musicalInstruments import get_base64, instruments
from flask_sqlalchemy import SQLAlchemy
from cs50 import SQL
import json
from instrumentsClass import addArtistList
app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TunePediaDB.db'
# db = SQLAlchemy(app)

db = SQL("sqlite:///TunePediaDB.db")


@app.route('/hello')
def hello():
    return jsonify({"message":"Hello World"})
    # return 'Hello, World!'

@app.route('/')
def index():
    return render_template('index.html')

@cross_origin
@app.route('/instruments')
def getInstruments():
    instrumentsDB = db.execute("select * from instrument")
    instrumentSerialized = list(map(lambda ins: addArtistList(ins,db=db).__dict__, instrumentsDB))
    print("instrumentosTest: ",json.dumps(instrumentSerialized,indent=4))
    return jsonify(instrumentSerialized)

@cross_origin
@app.route('/instruments/<string:name>')
def getInstByName(name):
    instrumentsDB = db.execute("select * from instrument where name = ? ", name)
    if len(instrumentsDB) == 0:
        return jsonify({"Excepcion":"Instrumento no encontrado"})
    instrumentSerialized = list(map(lambda ins: addArtistList(ins,db=db).__dict__, instrumentsDB))
    return instrumentSerialized


def getInstrument(name):
    instrumentFound = [ins for ins in instruments if ins["name"] == name]
    if len(instrumentFound) == 0:
        return jsonify({"Excepcion":"Instrumento no encontrado"})
    # if instrumentFound[0]["glbModel"]:
    #     base64_data = get_base64_data(instrumentFound[0]["glbModel"])
    #     instrumentFound[0]["base64Model"] = base64_data
    return jsonify(instrumentFound)


@cross_origin
@app.route('/models/<file_name>')
def obtener_archivo(file_name):
    file_path = 'media/glbModels/'+file_name
    return send_file(file_path)



def get_base64_data(file_name):
    file_path = 'media/glbModels/'+file_name
    with open(file_path, 'rb') as file:
        glb_data = file.read()
        base64_data = base64.b64encode(glb_data).decode('utf-8')
        base64_data_with_prefix = 'data:text/plain;charset=utf-8;base64,' + base64_data
        return base64_data_with_prefix

if __name__ == '__main__':
    app.run(debug = True, port = 4000)
