#!/usr/bin/env python3
"""to determine the best match with our supported language"""


from flask import Flask, request
from flask_babel import Babel, LocalSelector

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
