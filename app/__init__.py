from flask import Flask, g, abort


# Local Imports.
from .views import index


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index.index_bp)

    return app