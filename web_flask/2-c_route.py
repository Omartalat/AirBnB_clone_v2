#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def route_to_hbnb():
    """display "HBNB" """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def route_to_c(text):
    """display 'C'  followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return ("C {}".format(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
