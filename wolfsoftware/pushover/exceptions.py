"""
This module defines custom exceptions for the pushover package.

Classes:
    PushoverException: A custom exception class for handling Pushover-related errors.

Usage Example:
    from pushover.exceptions import PushoverException

    raise PushoverException("An error occurred")
"""


class PushoverException(Exception):
    """
    A custom exception class with a default error message.

    Attributes:
        message (str): The error message for the exception.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the PushoverException with an error message.

        Arguments:
            message (str): The error message for the exception.
        """
        super().__init__(message)
