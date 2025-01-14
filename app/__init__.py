from flask import Flask


def create_app(
) -> Flask:
    """
    Create Flask Application
    """
    app: Flask = Flask(__name__)

    app.config.from_object('config.Config')

    return app
