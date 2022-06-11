# tests/test_parse.py
from pathlib import Path


def get_path(filename: str) -> Path:
    return Path(f"./htmls/{filename}.html")


def get_text(path: Path) -> str:
    return path.read_text()


class TestParseNoun:
    def setup_method(self):
        path = get_path("dictionary")
        self.parsed_data = get_text(path)

    def test_get_part_of_speech(self):
        pass


class TestParseVerb:
    def setup_method(self):
        path = get_path("learn")
        self.parsed_data = get_text(path)

    def test_get_part_of_speech(self):
        pass


class TestParseAdjective:
    def setup_method(self):
        path = get_path("tremendous")
        self.parsed_data = get_text(path)

    def test_get_part_of_speech(self):
        pass


class TestParsePreposition:
    def setup_method(self):
        path = get_path("into")
        self.parsed_data = get_text(path)

    def test_get_part_of_speech(self):
        pass


class TestParseConjunction:
    def setup_method(self):
        path = get_path("although")
        self.parsed_data = get_text(path)

    def test_get_part_of_speech(self):
        pass


class TestParseNotFound:
    def setup_method(self):
        path = get_path("brah")
        self.parsed_data = get_text(path)

    def test_get_part_of_speech(self):
        pass


class TestParseMultiplePartOfSpeech:
    def setup_method(self):
        path = get_path("take")
        self.parsed_data = get_text(path)

    def test_get_part_of_speech(self):
        pass
