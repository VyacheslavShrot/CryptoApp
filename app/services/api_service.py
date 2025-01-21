from app.services.query_service import QueryService


class APIService(
    QueryService
):
    """
    Service for Base Flask API Functionality
    """

    @staticmethod
    def get_data(
            data: dict,
            params: list
    ) -> tuple:
        """
        Get Required Params from Data
        """

        response: tuple = tuple(
            data.get(param, None) for param in params
        )
        return response
