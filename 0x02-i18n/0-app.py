#!/usr/bin/env python3
""" An app for outputting "Welcome to Holberton"
    as a title page and Helloword as a Header
"""
from flask import Flask, render_template


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
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
