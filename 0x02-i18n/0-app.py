#!/usr/bin/python3
""" An app for outputting "Welcome to Holberton"
    as a title page and Helloword as a Header
"""
from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)

@app.route('/')
def index():
    """A funtion with a single / route pionting to an
    index.html file.
    Args:
        None
    Returns:
        To return hello world
    """
    greeting = (_("Hello, World!"))
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
