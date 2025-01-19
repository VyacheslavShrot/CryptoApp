from app.services.db_service import QueryBaseService


class QueryService(
    QueryBaseService
):
    """
    Queries into Database using Flask SQLAlchemy
    """

    def create_user(
            self,
    ):
        """
        Create User
        """
        ...
