# src/parse.py
from bs4 import BeautifulSoup


class Parse:
    @classmethod
    def parse(cls, fetch_data) -> dict:
        """
        Parse WEBLIO HTML to dict
        :return: dict - word info dict
        """
        soup = BeautifulSoup(fetch_data.text, "lxml")
        return {}
