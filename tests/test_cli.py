# tests/test_cli.py
import pytest

from src.cli import user_input


class TestUserInput:
    """
    test cli.user_input
    """

    def setup_method(self):
        self.input = [__name__]

    def test_user_input_one_word(self):
        self.input.append(":^)")
        parsed = user_input(self.input)
        assert parsed == ":^)"

    def test_user_input(self):
        self.input.extend(["why", "hello", "friends"])
        parsed = user_input(self.input)
        assert parsed == "why hello friends"

    def test_user_input_without_any_inputs(self):
        with pytest.raises(ValueError):
            user_input(self.input)
