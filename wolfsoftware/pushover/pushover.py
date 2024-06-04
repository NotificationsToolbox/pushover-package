"""
This module provides a class for interacting with the Pushover API.

It includes methods to send notifications, including regular, emergency, and group messages.
It also includes methods to list available sounds.

Classes:
    Pushover: A class to send notifications using the Pushover API.

Usage Example:
    pushover = Pushover(user_key="your_user_key", api_token="your_api_token")
    response = pushover.send_message(message="Hello, World!")
    print(response)
"""
from io import BufferedReader
from typing import Any, Dict, Optional

import requests

from requests.exceptions import HTTPError, RequestException

from .exceptions import PushoverException


class Pushover:
    """
    A class to send notifications using the Pushover API.

    Attributes:
        user_key (str): The Pushover user key.
        api_token (str): The Pushover API token.
        api_url (str): The base URL for sending messages.
    """

    def __init__(self, user_key: str, api_token: str, timeout: int = 10) -> None:
        """
        Initialize the Pushover class with user key and API token.

        Arguments:
            user_key (str): The Pushover user key.
            api_token (str): The Pushover API token.
            timeout (int): The requests timeout.
        """
        self.user_key: str = user_key
        self.api_token: str = api_token
        self.api_url = "https://api.pushover.net/1/messages.json"
        self.timeout: int = timeout

    def send_message(  # pylint: disable=too-many-arguments
            self,
            message: str,
            title: Optional[str] = None,
            url: Optional[str] = None,
            url_title: Optional[str] = None,
            priority: Optional[int] = 0,
            sound: Optional[str] = None,
            device: Optional[str] = None,
            attachment: Optional[str] = None) -> Dict:
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
        payload: Dict[str, Any] = {
            "token": self.api_token,
            "user": self.user_key,
            "message": message,
            "title": title,
            "url": url,
            "url_title": url_title,
            "priority": priority,
            "sound": sound,
            "device": device
        }

        try:
            if attachment:
                with open(attachment, "rb") as file:
                    files: Dict[str, BufferedReader] = {"attachment": file}
                    response: requests.Response = requests.post(self.api_url, data=payload, files=files, timeout=self.timeout)
            else:
                response = requests.post(self.api_url, data=payload, timeout=self.timeout)

            response.raise_for_status()
        except (HTTPError, RequestException) as e:
            raise PushoverException(f"Failed to send message: {e}") from e

        return response.json()

    def send_emergency_message(  # pylint: disable=too-many-arguments
            self, message: str,
            title: Optional[str] = None,
            url: Optional[str] = None,
            url_title: Optional[str] = None,
            retry: Optional[int] = 30,
            expire: Optional[int] = 3600,
            sound: Optional[str] = None,
            device: Optional[str] = None) -> Dict:
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
        payload: Dict[str, Any] = {
            "token": self.api_token,
            "user": self.user_key,
            "message": message,
            "title": title,
            "url": url,
            "url_title": url_title,
            "priority": 2,  # Priority 2 for emergency messages
            "retry": retry,
            "expire": expire,
            "sound": sound,
            "device": device
        }

        try:
            response: requests.Response = requests.post(self.api_url, data=payload, timeout=self.timeout)
            response.raise_for_status()
        except (HTTPError, RequestException) as e:
            raise PushoverException(f"Failed to send emergency message: {e}") from e

        return response.json()

    def send_group_message(  # pylint: disable=too-many-arguments
            self,
            message: str,
            group_key: str,
            title: Optional[str] = None,
            url: Optional[str] = None,
            url_title: Optional[str] = None,
            priority: Optional[int] = 0,
            sound: Optional[str] = None,
            device: Optional[str] = None,
            attachment: Optional[str] = None) -> Dict:
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
        payload: Dict[str, Any] = {
            "token": self.api_token,
            "user": group_key,
            "message": message,
            "title": title,
            "url": url,
            "url_title": url_title,
            "priority": priority,
            "sound": sound,
            "device": device
        }

        try:
            if attachment:
                with open(attachment, "rb") as file:
                    files: Dict[str, BufferedReader] = {"attachment": file}
                    response: requests.Response = requests.post(self.api_url, data=payload, files=files, timeout=self.timeout)
            else:
                response = requests.post(self.api_url, data=payload, timeout=self.timeout)

            response.raise_for_status()
        except (HTTPError, RequestException) as e:
            raise PushoverException(f"Failed to send group message: {e}") from e

        return response.json()

    def list_sounds(self) -> Dict:
        """
        List the available sounds from the Pushover API.

        Returns:
            dict: The response from the Pushover API.

        Raises:
            PushoverException: If the request to the Pushover API fails.
        """
        sounds_url = "https://api.pushover.net/1/sounds.json"
        params: Dict[str, str] = {
            "token": self.api_token
        }

        try:
            response: requests.Response = requests.get(sounds_url, params=params, timeout=self.timeout)
            response.raise_for_status()
        except (HTTPError, RequestException) as e:
            raise PushoverException(f"Failed to list sounds: {e}") from e

        return response.json()
