#!/usr/bin/env python3
""" you will implement a way to force a particular
    locale by passing the locale=fr parameter to your
    app’s URLs.
"""

from flask import Flask, request
from flask_babel import Babel #LocaleSelector

app = Flask(__name__)
babel = Babel(app)


app.config.from_object('config')


@babel.localeselector()
def get_locale():
    """ To get the language to be displayed """

    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == '__main__':
    app.run()
