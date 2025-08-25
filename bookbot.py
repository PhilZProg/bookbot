#! /usr/bin/env python3

import sys

from stats import *


def get_book_text(path):
    with open(path) as f:
        return f.read()


def usage():
    if len(sys.argv) != 2:
        print(f"Usage: bookbot.py <path_to_book>")
        sys.exit(1)


def main():
    usage()
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    print("----------- Word Count ----------")
    print(f"Found {wc(text)} total words")
    print("--------- Character Count -------")
    for c in convert(cc(text)):
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")


main()
