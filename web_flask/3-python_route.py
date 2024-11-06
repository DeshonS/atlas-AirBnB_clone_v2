#!/usr/bin/python3
"""Flask module that returns Hello HBNB"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', defaults={'text': 'is cool'}, strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return f"Python {text}"

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
