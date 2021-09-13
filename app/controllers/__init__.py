from flask import Blueprint

bp = Blueprint("views", __name__)

from . import views


def init_app(app):
    app.register_blueprint(bp)
