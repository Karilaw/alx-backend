#!/usr/bin/env python3
"""
This module sets up a basic Flask app with Babel for i18n/l10n.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    This function returns a user dictionary or
    None if the ID cannot be found or
    if login_as was not passed.
    """
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    This function is executed before all other functions.
    It uses get_user to find a user if any
    and set it as a global on flask.g.user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    This function determines the best
    match with our supported languages.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    This function renders the 5-index.html
    template when the root URL is accessed.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
