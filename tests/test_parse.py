# tests/test_parse.py
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from src.parse import Parse


def get_html(word_name: str) -> str:
    path = Path(f"./htmls/{word_name}.html")
    return path.read_text()


class TestParseNotFound:
    """
    NotFound word has no header, and any meaning
    so, this class has no Parse.parse_word_header, parse_meaning tests.
    """

    def setup_method(self):
        self.word_name = "notfound"
        self.html = get_html(self.word_name)
        self.soup = BeautifulSoup(self.html, "lxml")

    def test_word_name(self):
        word_info = Parse.parse(self.word_name, self.html)
        assert word_info["word_name"] == self.word_name

    def test_get_part_of_speech(self):
        word_info = Parse.parse(self.word_name, self.html)
        assert word_info["type_of_speech"] == []


class TestParseNoun:
    def setup_method(self):
        self.word_name = "dictionary"
        self.html = get_html(self.word_name)
        self.soup = BeautifulSoup(self.html, "lxml")

    def test_parse_word_header(self):
        word_info = {}
        Parse.parse_word_header(word_info, self.soup)

        assert word_info["main_meaning"] == "辞書、辞典"

    @pytest.mark.skip()
    def test_parse_meaning(self):
        word_info = {}
        Parse.parse_meaning(word_info, self.soup)

        assert word_info["noun"] == "辞書，辞典"


@pytest.mark.skip()
class TestParseVerb:
    def setup_method(self):
        pass

    def test_get_part_of_speech(self):
        pass


@pytest.mark.skip()
class TestParseAdjective:
    def setup_method(self):
        pass

    def test_get_part_of_speech(self):
        pass


@pytest.mark.skip()
class TestParsePreposition:
    def setup_method(self):
        self.word_name = "into"
        self.html = get_html(self.word_name)
        self.parsed = Parse.parse(self.word_name, self.html)

    def test_get_part_of_speech(self):
        pass


@pytest.mark.skip()
class TestParseConjunction:
    def setup_method(self):
        pass

    def test_get_part_of_speech(self):
        pass


class TestParseMultiplePartOfSpeeches:
    def setup_method(self):
        self.word_name = "take"
        self.html = get_html(self.word_name)
        self.soup = BeautifulSoup(self.html, "lxml")

    def test_parse_word_header(self):
        word_info = {}
        Parse.parse_word_header(word_info, self.soup)

        assert (
            word_info["main_meaning"]
            == "(手などで)取る、(…を)取る、つかむ、(…を)抱く、抱き締める、(わな・えさなどで)捕らえる、捕縛する、捕虜にする、(…を)(…で)捕らえる、占領する"
        )

    @pytest.mark.skip()
    def test_parse_meaning(self):
        word_info = {}
        Parse.parse_meaning(word_info, self.soup)

        assert word_info["noun"] == "辞書，辞典"
