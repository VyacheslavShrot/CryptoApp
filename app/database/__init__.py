from abc import ABC, abstractmethod


class Database(
    ABC
):
    """
    Abstract Database Class
    """

    @abstractmethod
    def db_init_app(self):
        """
        Connect with Database by flask_sqlalchemy
        """
        pass

    @abstractmethod
    def migrate_init_app(self):
        """
        Migrate with flask_migrate
        """
        pass
