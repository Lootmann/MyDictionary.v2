""" src/cache.py
A class to handle 'cache' files.

The meaning of 'handle' is as follows,
    save cache as json file
    load cache as dict from cache file

A cache file has these rules
    1. A cache file named 'word_name'.cache
    2. 'word_name' has some spaces like
        'endeavour', 'pull off', 'look forward to', ...
    3. A cache file is an ordinary json file.
"""
import json
from pathlib import Path


class Cache:
    CACHE_DIR_PATH = "~/.cache/mydict/"

    @classmethod
    def cache_dirpath(cls) -> Path:
        """
        get cache_dirpath. cache_dirpath is type of Pathlib

        :return: /home/user/.cache/mydict/ with Pathlib
        """
        return Path(cls.CACHE_DIR_PATH).expanduser()

    @classmethod
    def cache_path(cls, word_name: str) -> Path:
        """
        get cache file path.

        :param word_name:
        :return: /home/user/.cache/mydict/bruh.cache with Pathlib
        """
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
        """
        create a 'word_name'.cache file.

        :param word_name: str
        :param word_info: dict
        """
        path = cls.cache_path(word_name)

        with path.open("w", encoding="utf-8") as f:
            json.dump(word_info, f, ensure_ascii=False)

    @classmethod
    def load_cache(cls, word_name: str) -> dict:
        """
        Load 'word_name'.cache.

        :param word_name:
        :return:
        """
        path = cls.cache_path(word_name)

        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
