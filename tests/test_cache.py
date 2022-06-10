# tests/test_cache.py
import tempfile
from pathlib import Path

from src.cache import Cache


class TestHasCache:
    def setup_method(self):
        self.test_path = Path(Cache.CACHE_DIR_PATH).expanduser()
        self.tmp_dir = self.test_path.resolve()

    def test_when_cache_is_found(self):
        with tempfile.NamedTemporaryFile(dir=self.tmp_dir, suffix=".cache") as f:
            # get word_name, word_name is from tmp_file name without extension
            word_name = Path(f.name).resolve().stem
            assert Cache.has_cache(word_name) is True

    def test_when_cache_is_not_found(self):
        with tempfile.NamedTemporaryFile(dir=self.tmp_dir, suffix=".cache") as f:
            assert Cache.has_cache("tmp-random-file-name-but-not-found") is False
