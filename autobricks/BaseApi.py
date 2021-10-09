import requests
from requests.exceptions import HTTPError
import logging
from . import AutobricksLogging

logger = AutobricksLogging.get_logger(__name__)


def base_api_get(
    url: str, headers: dict, json: dict = None, data: dict = None, query: str = None
):

    if query:
        url = f"{url}?{query}"
    response = requests.get(url=url, headers=headers, json=json, data=data)

    try:
        response.raise_for_status()

    except HTTPError as e:

        msg = f"{e.response.status_code} error at {url} {e.response.text}"
        logger.error(msg)
        raise e

    return response


def base_api_post(url: str, headers: dict, json: dict = None, data: dict = None):

    response = requests.post(url=url, headers=headers, json=json, data=data)

    try:
        response.raise_for_status()

    except HTTPError as e:

        msg = f"{e.response.status_code} error at {url} {e.response.text}"
        logger.error(msg)
        raise e

    return response
