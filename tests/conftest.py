"""
This module contains fixtures for testing the Pushover class from the wolfsoftware.pushover package.

It includes fixtures for creating a Pushover instance, mocking the requests.post and requests.get methods,
and mocking file operations with builtins.open.
"""

from typing import Any, Generator, Union

from unittest.mock import AsyncMock, MagicMock, patch, mock_open

import pytest

from wolfsoftware.pushover import Pushover  # pylint: disable=import-error


@pytest.fixture
def pushover() -> Pushover:
    """
    Fixture for creating a Pushover instance.

    Returns:
        Pushover: A Pushover instance with test user key and API token.
    """
    return Pushover(user_key="test_user_key", api_token="test_api_token")  # nosec: B106


@pytest.fixture
def mock_post() -> Generator[Union[MagicMock, AsyncMock], Any, None]:
    """
    Fixture for mocking the requests.post method.

    Yields:
        unittest.mock.MagicMock: The mocked requests.post method.
    """
    with patch('requests.post') as mock:
        yield mock


@pytest.fixture
def mock_get() -> Generator[Union[MagicMock, AsyncMock], Any, None]:
    """
    Fixture for mocking the requests.get method.

    Yields:
        unittest.mock.MagicMock: The mocked requests.get method.
    """
    with patch('requests.get') as mock:
        yield mock


@pytest.fixture
def mock_file() -> Generator[None, Any, None]:
    """
    Fixture for mocking file operations with builtins.open.

    Yields:
        unittest.mock.MagicMock: The mocked builtins.open method.
    """
    with patch("builtins.open", mock_open(read_data="data")):
        yield
