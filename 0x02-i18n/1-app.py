#!/usr/bin/python3
"""To translate languages"""

from flask import render_template
from flask_bable import _

@app.route('/')
def index():
    greeting = _("Hello, World!")
    return render_template('1-index.html', greeting=greeting)
