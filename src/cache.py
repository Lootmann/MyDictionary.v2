# src/cache.py
from pathlib import Path


class Cache:
    CACHE_DIR_PATH = "~/.cache/mydict/"

    @classmethod
    def cache_dirpath(cls) -> Path:
        """
        get cache_dirpath
        :return: Path(CACHE_DIR_PATH)
        """
        return Path(cls.CACHE_DIR_PATH).expanduser()

    @classmethod
    def cache_path(cls, word_name: str) -> Path:
        return cls.cache_dirpath() / f"{word_name}.cache"

    @classmethod
    def create_cache_dir(cls) -> None:
        """
        create cache_dir if CACHE_DIR_PATH is not found.
        :return: None
        """
        dir_path = cls.cache_dirpath()
        if not dir_path.exists():
            dir_path.mkdir()

    @classmethod
    def has_cache(cls, word_name: str) -> bool:
        """
        has_cache finds 'word_name'.cache
        :param word_name: str
        :return: return True if word_name.cache has found
            return False if not
        """
        return cls.cache_path(word_name).exists()

    @classmethod
    def create_cache(cls, word_name: str, word_info: dict) -> None:
        dir_path = cls.cache_dirpath()
        return
