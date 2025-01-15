from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.database import Database


class PostgresDatabase(
    Database
):
    """
    Postgres Database
    """
    db: SQLAlchemy = None
    migrate: Migrate = None
    app: Flask = None

    def __init__(
            self,
            db: SQLAlchemy,
            migrate: Migrate,
            app: Flask,
            SQLALCHEMY_DATABASE_URI: str
    ):
        """
        Set SQLALCHEMY_DATABASE_URI into Flask APP Config
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.db = db
        self.migrate = migrate
        self.app = app

    def db_init_app(
            self
    ) -> None:
        """
        Init APP for DB
        """
        self.db.init_app(self.app)

    def migrate_init_app(
            self
    ) -> None:
        """
        Migrate APP
        """
        self.migrate.init_app(self.app, self.db)
