# src/main.py
from logging import config

import jstyleson

from src.cache import create_cache_dir


def init():
    # logger settings
    logger_filepath = "config/log_config.jsonc"

    with open(logger_filepath, "r") as f:
        log_conf = jstyleson.loads(f.read())

    config.dictConfig(log_conf)


def main():
    # 1. create cache_dir
    create_cache_dir()

    # 2. get user inputs called 'word_name'
    #       if fail to get user inputs, END :^)

    # 3. cache flow

    # 3.1 try to find 'word_name'.cache,
    #       if cache file is found, show this cache END :^)

    # 3.2 while not found 'word_name'.cache,
    #       create 'word_name'.cache

    # 4. create cache flow

    # 4.1 get fetch data from WEBLIO API
    #       fetch_data('word_name')

    # 4.1.1 if fail to fetch, END :^)
    # 4.1.2 if success to fetch, parse fetch data (HTML data)

    # 4.2 success to parse fetch data,
    #       create 'word_name'.cache using parsed HTML

    # 4.3 show this cache END :^)


if __name__ == "__main__":
    init()
    main()
