from random import choice as choice_


def _(word: str) -> str:
    return word.replace('_', ' ').lower()


all_words = list(
    map(
        _,
        open(
            'wordlists/en.txt',
            encoding='UTF-8',
        ).read().split(),
    ),
)


def choice() -> str:
    return choice_(all_words)
