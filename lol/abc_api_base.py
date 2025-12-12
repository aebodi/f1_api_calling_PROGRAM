from abc import ABC, abstractmethod
import os
import requests
import json


class APIBase(ABC):
    """
    Abstract Base Class for API interactions.
    All API subclasses must implement these methods.
    """

    def __init__(self):
        """Initialize base API attributes."""
        self.base_url = None
        self.headers = {}
        self.timeout = 10

    @abstractmethod
    def configure_api(self):
        """
        Configure API settings (base URL, headers, API key, etc.).
        Must be implemented by subclasses.

        This method should set:
            - self.base_url
            - self.headers
            - Any other API-specific configuration
        """
        pass

    @abstractmethod
    def format_output(self, data):
        """
        Format API data for console display.
        Must be implemented by subclasses.

        Args:
            data: Raw JSON data from the API

        Returns:
            str: Formatted string for console output
        """
        pass

    @abstractmethod
    def validate_input(self, **kwargs):
        """
        Validate user input before making API call.
        Must be implemented by subclasses.

        Args:
            **kwargs: Input parameters to validate

        Returns:
            bool: True if valid, False otherwise
        """
        pass

    def make_request(self, endpoint="", params=None, method="GET"):
        """
        Make an HTTP request to the API.

        Args:
            endpoint (str): API endpoint path (appended to base_url)
            params (dict): Query parameters for the request
            method (str): HTTP method (GET, POST, etc.)

        Returns:
            dict: Parsed JSON response from the API, or None if request fails
        """
        if not self.base_url:
            raise ValueError(
                "base_url not configured. Call configure_api() first.")

        url = f"{self.base_url}{endpoint}"

        try:
            if method.upper() == "GET":
                response = requests.get(
                    url,
                    params=params,
                    headers=self.headers,
                    timeout=self.timeout
                )
            elif method.upper() == "POST":
                response = requests.post(
                    url,
                    json=params,
                    headers=self.headers,
                    timeout=self.timeout
                )
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            self._handle_http_error(response.status_code, e)
        except requests.exceptions.Timeout:
            print(f"Error: Request timed out after {self.timeout} seconds.")
        except requests.exceptions.ConnectionError:
            print("Error: Connection failed. Please check your internet connection.")
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
        except json.JSONDecodeError:
            print("Error: Invalid JSON response from API.")

        return None

    def _handle_http_error(self, status_code, error):
        """
        Handle HTTP errors with appropriate messages.

        Args:
            status_code (int): HTTP status code
            error: The exception object
        """
        error_messages = {
            400: "Bad Request - The request was malformed or missing required parameters.",
            401: "Unauthorized - Invalid or missing API key.",
            403: "Forbidden - Access denied. Check rate limits or permissions.",
            404: "Not Found - The requested resource could not be found.",
            429: "Too Many Requests - Rate limit exceeded. Please wait before retrying.",
            500: "Internal Server Error - Server error occurred.",
            503: "Service Unavailable - The API is temporarily unavailable."
        }

        message = error_messages.get(status_code, f"HTTP Error {status_code}")
        print(f"Error: {message}")
        if status_code not in error_messages:
            print(f"Details: {error}")

    def fetch_data(self, **kwargs):
        """
        Fetch data from the API.
        This method can be overridden for custom behavior,
        or used directly by calling make_request().

        Args:
            **kwargs: Variable keyword arguments for API parameters

        Returns:
            dict: Parsed JSON response from the API
        """
        return self.make_request(params=kwargs)

    def get_data_and_format(self, **kwargs):
        """
        Convenience method to fetch and format data in one call.

        Args:
            **kwargs: Parameters to pass to fetch_data()

        Returns:
            str: Formatted output string
        """
        if not self.validate_input(**kwargs):
            return "Invalid input parameters."

        data = self.fetch_data(**kwargs)
        return self.format_output(data)
