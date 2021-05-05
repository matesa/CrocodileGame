from typing import Union

from . import database

collection = database.chats


def get(chat_id: int) -> Union[dict, bool]:
    return collection.find_one({'chat_id': chat_id}) or False


def update(chat_id: int, title: str) -> bool:
    find = get(chat_id)

    if not find:
        collection.insert_one(
            {
                'chat_id': chat_id,
                'title': title,
                'games': 1,
            },
        )
        return True

    collection.update_one(
        {'chat_id': chat_id},
        {
            '$set': {
                'title': title,
                'games': find['games'] + 1,
            },
        },
    )
    return True


def top_ten() -> Union[list, bool]:
    find = list(collection.find())

    if not find:
        return False

    _all = []

    for item in find:
        _all.append(
            {
                'chat_id': item['chat_id'],
                'games': item['games'],
            },
        )

    return sorted(_all, key=lambda x: x['games'])
