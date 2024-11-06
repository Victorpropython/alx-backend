#!/usr/bin/python3
"""Initializing all app"""


from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'  # Default timezone

babel = Babel(app)
