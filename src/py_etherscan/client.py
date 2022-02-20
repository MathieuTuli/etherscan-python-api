import requests
import logging

from .api.endpoint import Endpoint, EndpointStatus


class EmptyResponse(requests.exceptions.RequestException):
    """Empty Response"""


class InvalidAPIKey(requests.exceptions.RequestException):
    """Invalid API Key"""


class Client:
    def __init__(self) -> None:
        self.session = requests.session()

    def get(self, endpoint: Endpoint) -> Endpoint:
        try:
            response = self.session.get(endpoint.url)
        except requests.exceptions.ConnectionError as e:
            logging.critical("Something went wrong, cleaning up...")
            self.http_session.close()
            raise e

        if response.status_code == 200:
            if response.text:
                endpoint.process(response.json())
                if endpoint.status == EndpointStatus.OK:
                    return endpoint
                elif endpoint.status == EndpointStatus.NOTOK and \
                        endpoint.result == "Invalid API Key":
                    raise InvalidAPIKey(endpoint.result)
                else:
                    url = endpoint.url.replace(
                        '&', '\n    &').replace('?', '?\n    ')
                    raise EmptyResponse(
                        "Something went wrong. Check url parameters: " +
                        f"URL: \n{url}")
        raise requests.exceptions.RequestException(
            f"Response errored, status code: {response.status_code}")
