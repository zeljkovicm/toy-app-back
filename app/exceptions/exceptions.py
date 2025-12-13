class AuthenticationError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class ResourceNotFound(Exception):
    pass


class ValidationError(Exception):
    pass
