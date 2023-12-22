#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    text = text.replace('_', ' ')
    result_text = 'C {}'.format(text)
    return result_text

@app.route("/python/", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_text(text='is cool'):

    text = text.replace('_', ' ')
    format_text = 'Python {}'.format(text)
    return format_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
