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
