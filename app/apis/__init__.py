from typing import Any

from flask import request, jsonify, Flask

from app.services.logger import Logger


class APIMeta(type):
    """
    Meta Class for Register API
    """
    __available_methods: list = ['get', 'post', 'put', 'delete', 'patch']
    _register = True

    def __new__(
            cls,
            name,
            bases,
            dct
    ):
        if cls._register:
            # Function Register
            def register(self) -> None:
                """
                Register Route for Flask APP
                """

                # Get Current Methods
                methods: list = [
                    method_name.upper()
                    for method_name in dir(self)  # Iterate in ALL Class Methods
                    if callable(getattr(self, method_name))
                       and not method_name.startswith('_')  # Exclude 'magic' methods
                       and method_name in cls.__available_methods
                ]
                if not methods:
                    raise NotImplementedError(f"API Must Exist One of HTTP Methods -> {cls.__available_methods}")

                # Get Current Endpoint
                endpoint: str = getattr(self, "endpoint", None)
                if not endpoint:
                    raise NotImplementedError(f"{cls.__class__.__name__} Must Include endpoint Attr")

                self.app.add_url_rule(
                    endpoint,
                    view_func=self.dispatch_request,
                    methods=methods
                )

            # Function Dispatch Request
            def dispatch_request(self) -> Any:
                """
                Handles calling method (GET, POST...)
                """

                # Get Current HTTP Method
                method: str = request.method.lower()

                # Check if Exist Such Method
                handler = getattr(self, method, None)
                if handler:
                    return handler()

                return jsonify(
                    {
                        "error": f"Method {request.method} not allowed"
                    }
                ), 405

            # Update Methods
            dct['register'] = register
            dct['dispatch_request'] = dispatch_request
        else:
            raise NotImplementedError(f"{cls.__class__.__name__} Must Include _register Attr")

        return super().__new__(cls, name, bases, dct)


class APIRoute(
    Logger,
    metaclass=APIMeta
):
    endpoint = None

    def __init__(self, app: Flask):
        self.app = app

    def register(self) -> None:
        """
        Placeholder for the dynamically added 'register' method.
        Actual implementation is provided by the metaclass.
        """
        pass
