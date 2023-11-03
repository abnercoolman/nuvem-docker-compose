from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def animaisSitioCariri():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'infoAnimais'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT Animal_Nome, Animal_Raca FROM animaisSitioCariri')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


@app.route('/')
def index():
    data = animaisSitioCariri()
    return jsonify({'Dados dos animais do Sitio Cariri': data})


if __name__ == '__main__':
    app.run(host='0.0.0.0')