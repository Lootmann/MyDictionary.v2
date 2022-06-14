# tests/test_api.py
import pytest

from src.api import fetch_word


@pytest.mark.skipif(
    True, reason="when this test runs, this always gets HUGE html from Weblio."
)
class TestFetchWord:
    def test_fetch_word_is_success(self):
        # when fetch_data == 404 tells us that weblio site is down
        # so 'fetch_word test' needs only success version.
        fetch_data = fetch_word(word="hello")
        assert fetch_data.status_code == 200
