# src/parse.py
from bs4 import BeautifulSoup


class Parse:
    """
    Parsing Weblio HTML
    """

    @classmethod
    def parse(cls, fetch_data_text: str) -> dict:
        """
        Parse WEBLIO HTML to dict
        :return: dict - word info dict
        """
        soup = BeautifulSoup(fetch_data_text, "lxml")

        # main kiji
        main_block = soup.find("kijiWrp")

        return {}
