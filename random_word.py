# Generate random words
# =====================

import random

word_list = None


def create_list():
    global word_list
    with open("dictionary.txt") as fp:
        word_list = fp.readlines()


def get_word(quantity):
    if word_list is None:
        create_list()
    words = [random.choice(word_list).strip() for _ in range(quantity)]
    return words


if __name__ == '__main__':
    print(get_word(10))
