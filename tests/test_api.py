# tests/test_api.py
from src.api import fetch_word


class TestFetchWord:
    def test_fetch_word_is_success(self):
        # when fetch_data == 404 tells us that weblio site is down
        # so 'fetch_word test' needs only success version.
        fetch_data = fetch_word(word="hello")
        assert fetch_data.status_code == 200
