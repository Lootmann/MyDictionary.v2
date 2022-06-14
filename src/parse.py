# src/parse.py
from bs4 import BeautifulSoup


class Parse:
    """
    Parsing Weblio HTML
    """

    @classmethod
    def parse(cls, word_name: str, fetch_data_text: str) -> dict:
        """
        Parse WEBLIO HTML to dict
        :return: dict - word info dict
        """
        soup = BeautifulSoup(fetch_data_text, "lxml")

        # when 'word_name' is not found, this article has no 'kijiWrp' class
        if soup.find("table", id="anoOnnanoko"):
            return {f"{word_name}": "not found", "type_of_speech": []}

        # main kiji
        main_block = soup.find("kijiWrp")

        return {}
