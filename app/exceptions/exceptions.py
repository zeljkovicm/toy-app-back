class AuthenticationError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class ResourceNotFound(Exception):
    pass


class ValidationError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


class ExpiredTokenError(Exception):
    pass


class OrderNotFound(Exception):
    pass
