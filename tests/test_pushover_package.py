"""
This test module provides unit tests for the Pushover class from the wolfsoftware.pushover package using pytest.

It includes tests for versioning, sending messages, handling attachments, sending emergency messages,
sending group messages and listing sounds.
"""

from typing import Any, Dict, Optional

import importlib.metadata

from requests.exceptions import HTTPError

import pytest

from wolfsoftware.pushover import PushoverException


def test_version() -> None:
    """
    Test to ensure the version of the Package is set and not 'unknown'.

    This test retrieves the version of the package using importlib.metadata and asserts that the version
    is not None and not 'unknown'.
    """
    version: Optional[str] = None

    try:
        version = importlib.metadata.version('wolfsoftware.pushover')
    except importlib.metadata.PackageNotFoundError:
        version = None

    assert version is not None, "Version should be set"  # nosec: B101
    assert version != 'unknown', f"Expected version, but got {version}"  # nosec: B101


def test_send_message_success(pushover, mock_post) -> None:
    """
    Test successful sending of a message using the Pushover instance.

    This test mocks the requests.post method to return a successful status code and response.
    It asserts that the response is as expected and that the post request was called once.
    """
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": 1}

    response: Dict = pushover.send_message(message="Test message")

    assert response == {"status": 1}  # nosec: B101
    mock_post.assert_called_once()


def test_send_message_failure(pushover, mock_post) -> None:
    """
    Test failure in sending a message using the Pushover instance.

    This test mocks the requests.post method to return a failure status code and raises an HTTPError.
    It asserts that a PushoverException is raised with the appropriate error message.
    """
    mock_response: Any = mock_post.return_value
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = HTTPError("Bad Request")

    with pytest.raises(PushoverException, match="Failed to send message: Bad Request"):
        pushover.send_message(message="Test message")


def test_send_message_with_attachment_success(pushover, mock_post, mock_file) -> None:  # pylint: disable=unused-argument
    """
    Test successful sending of a message with an attachment using the Pushover instance.

    This test mocks the requests.post method to return a successful status code and response.
    It asserts that the response is as expected and that the post request was called once.
    """
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": 1}

    response: Dict = pushover.send_message(message="Test message", attachment="path/to/file")

    assert response == {"status": 1}  # nosec: B101
    mock_post.assert_called_once()


def test_send_message_with_attachment_failure(pushover, mock_post, mock_file) -> None:  # pylint: disable=unused-argument
    """
    Test failure in sending a message with an attachment using the Pushover instance.

    This test mocks the requests.post method to return a failure status code and raises an HTTPError.
    It asserts that a PushoverException is raised with the appropriate error message.
    """
    mock_response: Any = mock_post.return_value
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = HTTPError("Bad Request")

    with pytest.raises(PushoverException, match="Failed to send message: Bad Request"):
        pushover.send_message(message="Test message", attachment="path/to/file")


def test_send_emergency_message_success(pushover, mock_post) -> None:
    """
    Test successful sending of an emergency message using the Pushover instance.

    This test mocks the requests.post method to return a successful status code and response.
    It asserts that the response is as expected and that the post request was called once.
    """
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": 1}

    response: Dict = pushover.send_emergency_message(message="Emergency message")

    assert response == {"status": 1}  # nosec: B101
    mock_post.assert_called_once()


def test_send_emergency_message_failure(pushover, mock_post) -> None:
    """
    Test failure in sending an emergency message using the Pushover instance.

    This test mocks the requests.post method to return a failure status code and raises an HTTPError.
    It asserts that a PushoverException is raised with the appropriate error message.
    """
    mock_response: Any = mock_post.return_value
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = HTTPError("Bad Request")

    with pytest.raises(PushoverException, match="Failed to send emergency message: Bad Request"):
        pushover.send_emergency_message(message="Emergency Test message")


def test_send_group_message_success(pushover, mock_post) -> None:
    """
    Test successful sending of a group message using the Pushover instance.

    This test mocks the requests.post method to return a successful status code and response.
    It asserts that the response is as expected and that the post request was called once.
    """
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": 1}

    response: Dict = pushover.send_group_message(message="Group message", group_key="test_group_key")

    assert response == {"status": 1}  # nosec: B101
    mock_post.assert_called_once()


def test_send_group_message_with_attachment_success(pushover, mock_post, mock_file) -> None:  # pylint: disable=unused-argument
    """
    Test successful sending of a message with an attachment using the Pushover instance.

    This test mocks the requests.post method to return a successful status code and response.
    It asserts that the response is as expected and that the post request was called once.
    """
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": 1}

    response: Dict = pushover.send_group_message(message="Test message", group_key="test_group_key", attachment="path/to/file")

    assert response == {"status": 1}  # nosec: B101
    mock_post.assert_called_once()


def test_send_group_message_with_attachment_failure(pushover, mock_post, mock_file) -> None:  # pylint: disable=unused-argument
    """
    Test failure in sending a message with an attachment using the Pushover instance.

    This test mocks the requests.post method to return a failure status code and raises an HTTPError.
    It asserts that a PushoverException is raised with the appropriate error message.
    """
    mock_response: Any = mock_post.return_value
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = HTTPError("Bad Request")

    with pytest.raises(PushoverException, match="Failed to send group message: Bad Request"):
        pushover.send_group_message(message="Test message", group_key="test_group_key", attachment="path/to/file")


def test_send_group_message_failure(pushover, mock_post) -> None:
    """
    Test failure in sending a group message using the Pushover instance.

    This test mocks the requests.post method to return a failure status code and raises an HTTPError.
    It asserts that a PushoverException is raised with the appropriate error message.
    """
    mock_response: Any = mock_post.return_value
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = HTTPError("Bad Request")

    with pytest.raises(PushoverException, match="Failed to send group message: Bad Request"):
        pushover.send_group_message(message="Group message", group_key="test_group_key")


def test_list_sounds_success(pushover, mock_get) -> None:
    """
    Test successful retrieval of available sounds using the Pushover instance.

    This test mocks the requests.get method to return a successful status code and response.
    It asserts that the response is as expected and that the get request was called once.
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"sounds": {"pushover": "Pushover (default)"}}

    response: Dict = pushover.list_sounds()

    assert response == {"sounds": {"pushover": "Pushover (default)"}}  # nosec: B101
    mock_get.assert_called_once()


def test_list_sounds_failure(pushover, mock_get) -> None:
    """
    Test failure in retrieving available sounds using the Pushover instance.

    This test mocks the requests.get method to return a failure status code and raises an HTTPError.
    It asserts that a PushoverException is raised with the appropriate error message.
    """
    mock_response: Any = mock_get.return_value
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = HTTPError("Bad Request")

    with pytest.raises(PushoverException, match="Failed to list sounds: Bad Request"):
        pushover.list_sounds()
