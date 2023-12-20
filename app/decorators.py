from functools import wraps
from flask import abort
from flask_login import current_user


def authorization_required(permissions):
    """Decorator to provide authorization checking for routes

    Args:
        permissions (enum.Flag): permission bitmask fileds required
    """
    def wrapper(func):
        @wraps(func)
        def wrapped_function(*arg, **kwargs):
            if not current_user.role.permissions & permissions:
                abort(403)
            return func(*arg, **kwargs)
        return wrapped_function

    return wrapper
