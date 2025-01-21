from flask import jsonify, request

from app.apis import APIRoute
from app.services.user import UserAPIService


class RegisterUser(
    APIRoute,
    UserAPIService
):
    """
    Post API for Register User
    """
    endpoint = "/user/register"

    def post(
            self
    ) -> jsonify:
        try:
            # Get Data
            data: dict = request.get_json()

            response, status_code = self.register_user(
                data=data
            )

            return jsonify(
                response
            ), status_code
        except Exception as e:
            self.logger.error(f"An Unexpected Error Occurred while Register User | {e}")
