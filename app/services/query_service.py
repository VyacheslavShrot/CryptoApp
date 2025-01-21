from app.models.user import User
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

    def get_user(
            self,
            username: str
    ):
        """
        Get User Object by username
        """
        user: User = User.query.filter_by(username=username).first()
