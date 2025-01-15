from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.database.postgresql_db import PostgresDatabase
from app.services.db_service import DatabaseService


def create_app(
) -> Flask:
    """
    Create Flask Application
    """
    app: Flask = Flask(__name__)

    app.config.from_object('config.Config')

    """
    Init Database and Migrations
    """
    db: SQLAlchemy = SQLAlchemy()
    migrate: Migrate = Migrate()

    SQLALCHEMY_DATABASE_URI: str = app.config.get("SQLALCHEMY_DATABASE_URI", None)

    database = DatabaseService(
        db=db,
        migrate=migrate,
        app=app,
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI if SQLALCHEMY_DATABASE_URI else f'postgresql://{app.config["POSTGRES_USER"]}:{app.config["POSTGRES_PASSWORD"]}@postgres:5432/default_name'
    )
    database.init_db_migrate()

    return app
