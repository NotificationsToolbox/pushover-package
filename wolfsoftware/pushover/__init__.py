"""
A Python package for interacting with the Pushover API.

This package provides a class and custom exception for sending notifications
using the Pushover API, including support for regular, emergency, and group messages.

Attributes:
    __version__ (str): The version of the package, retrieved from the package metadata.
    __all__ (list[str]): A list of all public symbols that the module exports.

Classes:
    PushoverException: A custom exception for handling Pushover-related errors.
    Pushover: A class to send notifications using the Pushover API.

Usage Example:
    from pushover import Pushover
    pushover = Pushover(user_key="your_user_key", api_token="your_api_token")
    response = pushover.send_message(message="Hello, World!")
    print(response)
"""

import importlib.metadata

from .exceptions import PushoverException
from .pushover import Pushover

try:
    __version__: str = importlib.metadata.version('wolfsoftware.pushover')
except importlib.metadata.PackageNotFoundError:
    __version__ = 'unknown'

__all__: list[str] = [
    'Pushover',
    'PushoverException'
]
