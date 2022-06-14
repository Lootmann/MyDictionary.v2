# src/main.py
import sys
from logging import config

import jstyleson

import api
import cli
from cache import Cache
from cli import user_input
from parse import Parse


def init():
    # logger settings
    logger_filepath = "config/log_config.jsonc"

    with open(logger_filepath, "r") as f:
        log_conf = jstyleson.loads(f.read())

    config.dictConfig(log_conf)


def main():
    Cache.create_cache_dir()

    word_name = user_input(sys.argv)

    if Cache.has_cache(word_name):
        print(f">>> found cache: {word_name}.cache")
        cached_dict = Cache.load_cache(word_name)
        cli.prettify(cached_dict)
        return

    print(f">>> fetch data: {word_name} from WEBLIO")
    fetch_data = api.fetch_word(word_name)
    parsed_dict = Parse.parse(word_name, fetch_data.text)

    print(f">>> create cache: {word_name}.cache")
    Cache.create_cache(word_name, parsed_dict)
    cli.prettify(parsed_dict)


if __name__ == "__main__":
    init()
    main()
