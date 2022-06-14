# src/parse.py
from bs4 import BeautifulSoup


class Parse:
    """
    Parsing Weblio HTML
    """

    @classmethod
    def parse_word_header(cls, word_info: dict, soup):
        """
        get some items from word_header

        All type_of_speech:
            word_header

        Verb:
            conjugation_table: only when word has verb

        :param word_info: dict
        :param soup: BeautifulSoup Object using Weblio HTML
        :return: None
        """
        word_header = soup.find("div", id="summary")

        main_meaning = (
            word_header.find("div", class_="summaryM")
            .find("span", class_="content-explanation ej")
            .text
        )

        # TODO: update word_info 'conjugation_table'
        word_info["main_meaning"] = main_meaning.strip()

    @classmethod
    def parse_meaning(cls, word_info: dict, soup):
        # TODO: refactoring Like { "noun":[] "verb": [], ... }
        word_info["word_meaning"] = []

        level0 = soup.find_all("div", attrs={"class": "level0"})
        for item in level0:
            line = ["", "", "", "", "", ""]
            lvl_knenjsub = item.find("div", attrs={"class": "KnenjSub"})
            crosslink = item.findAll("a", attrs={"class": "crosslink"})
            lvl_uah = item.find("span", attrs={"class": "lvlUAH"})
            lvl_nh = item.find("p", attrs={"class": "lvlNH"})
            lvl_ah = item.find("p", attrs={"class": "lvlAH"})
            lvl_b = item.find("p", attrs={"class": "lvlB"})

            if lvl_knenjsub:
                line[0] = lvl_knenjsub.text
            if crosslink:
                line[1] = " ".join(item.text for item in crosslink)
            if lvl_uah:
                line[2] = lvl_uah.text
            if lvl_nh:
                line[3] = lvl_nh.text
            if lvl_ah:
                line[4] = lvl_ah.text
            if lvl_b:
                line[5] = lvl_b.text

            word_info["word_meaning"].append(line)

    @classmethod
    def parse(cls, word_name: str, fetch_data_text: str) -> dict:
        """
        Parse WEBLIO HTML to dict
        :return: dict - word info dict
        """
        soup = BeautifulSoup(fetch_data_text, "lxml")

        # when 'word_name' is not found, this article has no 'kijiWrp' class
        if soup.find("table", id="anoOnnanoko"):
            return {"word_name": "notfound", "type_of_speech": []}

        # main flow
        word_info = {"word_name": word_name}

        # word header
        cls.parse_word_header(word_info, soup)

        # type_of_speech, meanings
        cls.parse_meaning(word_info, soup)

        return word_info
