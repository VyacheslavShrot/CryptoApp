from flask_sqlalchemy import SQLAlchemy

from app import PostgresDatabase


class DatabaseService(
    PostgresDatabase
):
    """
    Main DB
    Use Inheritance from Database which want to Use
    """

    def init_db_migrate(
            self
    ) -> None:
        """
        Init DB and Migrate
        """

        self.db_init_app()
        self.migrate_init_app()


class QueryBaseService:
    db: SQLAlchemy = SQLAlchemy()

    def commit(self) -> None:
        """
        Commit Database Changes
        """

        self.db.session.commit()

    def add_and_commit(
            self,
            models_object
    ) -> None:
        """
        Add Object and Save
        :param models_object: User or Strategy -> Some Instance of Models Class
        """

        self.db.session.add(models_object)
        self.commit()

    def delete_and_commit(
            self,
            models_object
    ) -> None:
        """
        Delete Object from DB
        :param models_object: User or Strategy -> Some Instance of Models Class
        """

        self.db.session.delete(models_object)
        self.commit()
