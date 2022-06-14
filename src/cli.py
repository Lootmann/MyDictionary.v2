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


def prettify(word_info: dict) -> None:
    """prettify print word_info

    :param word_info: dict - key: values are followings
        "word_name": str
        "main_meaning": str
        "conjugation_table": str when word has verb
        "word_meaning": list
    :return: None - print info to stdout console
    """
    print("word_name : ", word_info["word_name"], end="\n\n")
    print("main_meaning : ", word_info["main_meaning"], end="\n\n")

    for meaning in word_info["word_meaning"]:
        print(" ".join(meaning))
