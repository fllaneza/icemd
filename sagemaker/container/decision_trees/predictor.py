
# Este script implementa un servidor con Flask para realizar la inferencia

from __future__ import print_function

import os
import json
import pickle
import StringIO
import sys

import flask

import pandas as pd

ROOT_PATH = '/opt/ml/'
MODEL_PATH = os.path.join(ROOT_PATH, 'model')
MODEL_NAME = "decision-tree-model"

# Creamos una clase para cargar el modelo y realizar predicciones

class ScoringService(object):
    # Variable para guardar el modelo una vez cargado
    model = None                

    @classmethod
    def get_model(cls):
        """Obtenemos el modelo para esta instancia, cargándolo si no lo está ya"""
        if cls.model == None:
            with open(os.path.join(MODEL_PATH, MODEL_NAME +'.pkl'), 'r') as inp:
                cls.model = pickle.load(inp)
        return cls.model

    @classmethod
    def predict(cls, input):
        """Realiza y devuelve las predicciones para el 'input'

        Args:
            input (Pandas DataFrame): las variables explicativas con las que realizar las predicciones"""
        clf = cls.get_model()
        return clf.predict(input)

# El app de Flask para servir las predicciones
app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    """Detemina si el contenedor está sano y activo"""
    health = ScoringService.get_model() is not None  

    status = 200 if health else 404
    return flask.Response(response='\n', status=status, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():
    """Realiza la inferencia en modo batch para un input en formato CSV"""
    data = None

    # Convertimos de CSV a Pandas
    if flask.request.content_type == 'text/csv':
        data = flask.request.data.decode('utf-8')
        s = StringIO.StringIO(data)
        data = pd.read_csv(s, header=None)
    else:
        return flask.Response(response='Este predictor solo soporta inputs en formato CSV', status=415, mimetype='text/plain')

    print('Existen {} registros sobre los que predecir'.format(data.shape[0]))

    # Realia las predicciones
    predictions = ScoringService.predict(data)

    # Convierte de Numpy a CSV
    out = StringIO.StringIO()
    pd.DataFrame({'results':predictions}).to_csv(out, header=False, index=False)
    result = out.getvalue()

    return flask.Response(response=result, status=200, mimetype='text/csv')
