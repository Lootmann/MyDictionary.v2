# src/api.py
from logging import getLogger

import requests

logger = getLogger(__name__)

WEBLIO_URL = "https://ejje.weblio.jp/content/{word:}"


def fetch_word(word: str):
    """
    Fetch word information from WEBLIO_API
    :param word:str
    :return: fetch WEBLIO HTML
    """
    fetch_data = requests.get(WEBLIO_URL.format(word=word))

    try:
        # NOTE: This is very rare case the weblio site is down
        fetch_data.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.debug(e)

    return fetch_data
