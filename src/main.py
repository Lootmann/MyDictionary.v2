# src/main.py
from logging import config

import jstyleson


def init():
    # logger settings
    logger_filepath = "config/log_config.jsonc"

    with open(logger_filepath, "r") as f:
        log_conf = jstyleson.loads(f.read())

    config.dictConfig(log_conf)


def main():
    pass


if __name__ == "__main__":
    init()
    main()
