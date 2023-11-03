# -*- coding: utf-8 -*-
#!usr/bin/env python3

"""


"""
import logging
import os
from flask import Flask, request, render_template, redirect, url_for, json, jsonify

app = Flask(__name__, template_folder='.')
redis = Redis(host='redis', port=6379)

logging.basicConfig(filename='main.log', level=logging.INFO)

animal_data = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        animal_id = request.form['animal-id']
        animal_raca = request.form['animal-raca']
        animal_dataNasc = request.form['animal-dataNasc']
        animal_sexo = request.form['animal-sexo']
        animal_peso = request.form['animal-peso']

        animal_data.append({
            'ID': animal_id,
            'Raça': animal_raca,
            'Data de Nascimento': animal_dataNasc,
            'Sexo': animal_sexo,
            'Peso (kg)': animal_peso
        })

        return redirect(url_for('success'))

    return render_template('index.html')


@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')


@app.route('/view_data', methods=['GET'])
def view_data():
    return render_template('view_data.html', animal_data=animal_data)


def get_env_or_default(ENV: str, default: str):
    """Gets environment variables or sets a default

    Args:
        ENV (str): the Env variable
        default (str): the default value to return if ENV is not find

    Returns:
        The value of ENV or default
    """
    if os.environ.get(ENV):
        app.logger.info("ENV {}".format(os.environ.get(ENV)))
        return os.environ.get(ENV)
    return default


if __name__ == '__main__':
    app_args = {}

    app_args["host"] = get_env_or_default("A_HOST", '0.0.0.0')
    app_args["port"] = int(get_env_or_default("A_PORT", 5001))
    app_args["debug"] = bool(get_env_or_default("A_DEBUG", True))

    app.run(**app_args)
