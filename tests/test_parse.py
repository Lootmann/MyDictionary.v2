# tests/test_parse.py
from pathlib import Path

import pytest

from src.parse import Parse


def get_path(filename: str) -> Path:
    return Path(f"./htmls/{filename}.html")


def get_html(path: Path) -> str:
    return path.read_text()


class TestParseNotFound:
    def setup_method(self):
        self.word_name = "notfound"
        path = get_path(self.word_name)
        self.html = get_html(path)
        self.parsed = Parse.parse(self.word_name, self.html)

    def test_has_no_definitions(self):
        assert self.parsed[self.word_name] == "not found"

    def test_get_part_of_speech(self):
        assert self.parsed["type_of_speech"] == []


@pytest.mark.skip()
class TestParseNoun:
    def setup_method(self):
        path = get_path("dictionary")
        self.parsed_data = get_html(path)

    def test_get_part_of_speech(self):
        pass


@pytest.mark.skip()
class TestParseVerb:
    def setup_method(self):
        path = get_path("learn")
        self.parsed_data = get_html(path)

    def test_get_part_of_speech(self):
        pass


@pytest.mark.skip()
class TestParseAdjective:
    def setup_method(self):
        path = get_path("tremendous")
        self.parsed_data = get_html(path)

    def test_get_part_of_speech(self):
        pass


@pytest.mark.skip()
class TestParsePreposition:
    def setup_method(self):
        self.word_name = "into"
        path = get_path(self.word_name)
        self.html = get_html(path)
        self.parsed = Parse.parse(self.word_name, self.html)

    def test_get_part_of_speech(self):
        pass


@pytest.mark.skip()
class TestParseConjunction:
    def setup_method(self):
        path = get_path("although")
        self.parsed_data = get_html(path)

    def test_get_part_of_speech(self):
        pass


@pytest.mark.skip()
class TestParseMultiplePartOfSpeech:
    def setup_method(self):
        path = get_path("take")
        self.parsed_data = get_html(path)

    def test_get_part_of_speech(self):
        pass
