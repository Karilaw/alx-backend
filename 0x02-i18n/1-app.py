#!/usr/bin/env python3
"""
This module sets up a basic Flask
app with Babel for i18n/l10n.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration class for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    This function renders the 1-index.html
    template when the root URL is accessed.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
