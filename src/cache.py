# src/cache.py
from pathlib import Path

CACHE_DIR_PATH = "~/.cache/mydict/"


def create_cache_dir() -> None:
    """
    create cache_dir if CACHE_DIR_PATH is not found.
    :return: None
    """
    dir_path = Path(CACHE_DIR_PATH).expanduser()
    if dir_path.exists():
        dir_path.mkdir()


def has_cache(word_name: str) -> bool:
    """
    has_cache finds 'word_name'.cache
    :param word_name: str
    :return: return True if word_name.cache has found
        return False if not
    """
    cache_path = Path(CACHE_DIR_PATH) / f"{word_name}.cache"
    abs_cache_path = cache_path.expanduser()
    return abs_cache_path.exists()
