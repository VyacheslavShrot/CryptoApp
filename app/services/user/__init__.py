from typing import Any

from app.services.api_service import APIService


class UserAPIService(
    APIService
):
    """
    Service for User APIs
    """

    def register_user(
            self,
            data: dict
    ) -> tuple:
        """
        Register User API Functionality
        """

        # Get Credentials for Registration
        username, password = self.get_data(
            data=data,
            params=[
                "username", "password"
            ]
        )
        if not username or not password:
            return {
                       "error": "'username' and 'password' are Required Params"
                   }, 400

        return {
                   "success": True
               }, 201
