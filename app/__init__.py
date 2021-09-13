import os
from flask import Flask

from app import controllers
from app import models


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    controllers.init_app(app)
    models.init_app(app)

    return app
