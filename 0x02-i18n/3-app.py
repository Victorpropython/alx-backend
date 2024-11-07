#!/usr/bin/env python3
"""function to parametrize your templates"""

from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    title = _("home_title")
    header = _("home_header")
    return render_template('3-index.html', title=title, header=header)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
