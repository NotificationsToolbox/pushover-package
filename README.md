<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/NotificationsToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/notificationstoolbox/black-and-white-circle-256.png" alt="NotificationsToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/NotificationsToolbox/pushover-package/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/NotificationsToolbox/pushover-package/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/NotificationsToolbox/pushover-package/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/NotificationsToolbox/pushover-package?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/NotificationsToolbox/pushover-package">
        <img src="https://img.shields.io/github/created-at/NotificationsToolbox/pushover-package?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/NotificationsToolbox/pushover-package/releases/latest">
        <img src="https://img.shields.io/github/v/release/NotificationsToolbox/pushover-package?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/NotificationsToolbox/pushover-package/releases/latest">
        <img src="https://img.shields.io/github/release-date/NotificationsToolbox/pushover-package?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/NotificationsToolbox/pushover-package/releases/latest">
        <img src="https://img.shields.io/github/commits-since/NotificationsToolbox/pushover-package/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/NotificationsToolbox/pushover-package/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/NotificationsToolbox/pushover-package/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/NotificationsToolbox/pushover-package/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/NotificationsToolbox/pushover-package/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This project provides a Python interface to the Pushover API, allowing you to send notifications through the Pushover service. The package
supports sending messages, emergency messages, and group messages, as well as listing available sounds.

## Installation

To install the package, you can use `pip`:

```bash
pip install wolfsoftware-pushover
```

## Usage

Here's a basic example of how to use the Pushover package:

```python
from wolfsoftware.pushover import Pushover

# Initialize the Pushover instance
pushover = Pushover(user_key='your_user_key', api_token='your_api_token')

# Send a message
response = pushover.send_message(message='Hello, this is a test message!')
print(response)
```

## API

### Pushover Class

The `Pushover` class provides methods to interact with the Pushover API. 

#### Initialization

```python
pushover = Pushover(user_key='your_user_key', api_token='your_api_token')
```

### Methods

#### send_message

Sends a message through Pushover.

```python
def send_message(message: str, title: Optional[str] = None, url: Optional[str] = None, url_title: Optional[str] = None, priority: Optional[int] = 0, sound: Optional[str] = None, device: Optional[str] = None, attachment: Optional[str] = None) -> dict:
    """
    Send a message using the Pushover API.

    Arguments:
        message (str): The message content.
        title (str, optional): The message title.
        url (str, optional): A supplementary URL to show with the message.
        url_title (str, optional): A title for the supplementary URL.
        priority (int, optional): The priority of the message.
        sound (str, optional): The name of the sound to play with the message.
        device (str, optional): The device name to send the message to.
        attachment (str, optional): Path to an attachment file.

    Returns:
        dict: The response from the Pushover API.

    Raises:
        PushoverException: If the request to the Pushover API fails.
    """
```

#### send_emergency_message

Sends an emergency message through Pushover.

```python
def send_emergency_message(message: str, title: Optional[str] = None, url: Optional[str] = None, url_title: Optional[str] = None, retry: Optional[int] = 30, expire: Optional[int] = 3600, sound: Optional[str] = None, device: Optional[str] = None) -> Dict:
    """
    Send an emergency message using the Pushover API.

    Arguments:
        message (str): The message content.
        title (str, optional): The message title.
        url (str, optional): A supplementary URL to show with the message.
        url_title (str, optional): A title for the supplementary URL.
        retry (int, optional): How often (in seconds) to retry the message.
        expire (int, optional): How long (in seconds) before the message expires.
        sound (str, optional): The name of the sound to play with the message.
        device (str, optional): The device name to send the message to.

    Returns:
        dict: The response from the Pushover API.

    Raises:
        PushoverException: If the request to the Pushover API fails.
    """
```

#### send_group_message

Sends a message to a group through Pushover.

```python
def send_group_message(message: str, group_key: str, title: Optional[str] = None, url: Optional[str] = None, url_title: Optional[str] = None, priority: Optional[int] = 0, sound: Optional[str] = None, device: Optional[str] = None, attachment: Optional[str] = None) -> Dict:
    """
    Send a message to a group using the Pushover API.

    Arguments:
        message (str): The message content.
        group_key (str): The Pushover group key.
        title (str, optional): The message title.
        url (str, optional): A supplementary URL to show with the message.
        url_title (str, optional): A title for the supplementary URL.
        priority (int, optional): The priority of the message.
        sound (str, optional): The name of the sound to play with the message.
        device (str, optional): The device name to send the message to.
        attachment (str, optional): Path to an attachment file.

    Returns:
        dict: The response from the Pushover API.

    Raises:
        PushoverException: If the request to the Pushover API fails.
    """
```

#### list_sounds

Lists available sounds.

```python
def list_sounds(self) -> dict:
    """
    List the available sounds from the Pushover API.

    Returns:
        dict: The response from the Pushover API.

    Raises:
        PushoverException: If the request to the Pushover API fails.
    """
```

## Testing

The project includes unit tests for all functionalities provided by the `Pushover` class. The tests use the `pytest` framework and mock
the `requests` library to simulate API responses.

### Unit Tests

To run the unit tests, you can use `pytest`:

```bash
pytest
```

### Fixtures

The tests use several fixtures to set up the testing environment:

- `pushover`: Provides a `Pushover` instance with test credentials.
- `mock_post`: Mocks the `requests.post` method.
- `mock_get`: Mocks the `requests.get` method.
- `mock_file`: Mocks file operations.

Example test functions:

```python
def test_send_message_success(pushover, mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": 1}

    response = pushover.send_message(message="Test message")

    assert response == {"status": 1}
    mock_post.assert_called_once()
```

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
