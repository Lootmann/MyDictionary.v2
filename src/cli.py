# src/cli.py
import argparse
from typing import List


def user_input(argv: List[str]) -> str:
    """
    Ger user_input
    :param: None
    :return: str - word_name
    """
    # when no arguments, raise ValueError
    if len(argv) == 1:
        raise ValueError("need arguments")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word",
        nargs="+",
        type=str,
        help="input english word that you want to know the definition",
    )

    # get command-line args from sys.argv automatically
    args = parser.parse_args(argv)
    return " ".join(args.word[1:])
