from time import time

from telegram import User
from telegram.ext import CallbackContext

from words import choice


def make_sure_in_game(context: CallbackContext) -> bool:
    game = context.chat_data.get('game')

    if game:
        if (time() - game['start']) >= 300:
            end_game(context)
            raise Exception('There is no game going on.')

        return True

    raise Exception('There is no game going on.')


def make_sure_not_in_game(context: CallbackContext) -> bool:
    game = context.chat_data.get('game')

    if game:
        if (time() - game['start']) >= 300:
            end_game(context)
            return True

        raise Exception('There is a game going on.')

    return True


def requires_game_running(func):
    def wrapper(*args, **kwargs):
        context = [
            item for item in args if isinstance(item, CallbackContext)
        ][0]
        make_sure_in_game(context)
        return func(*args, **kwargs)
    return wrapper


def requires_game_not_running(func):
    def wrapper(*args, **kwargs):
        context = [
            item for item in args if isinstance(item, CallbackContext)
        ][0]
        make_sure_not_in_game(context)
        return func(*args, **kwargs)
    return wrapper


@requires_game_not_running
def new_game(host: User, context: CallbackContext) -> bool:
    context.chat_data['game'] = {
        'start': time(),
        'host': host,
        'word': choice(),
    }
    return True


@requires_game_running
def get_game(context: CallbackContext) -> dict:
    return context.chat_data['game']


@requires_game_running
def next_word(context: CallbackContext) -> str:
    context.chat_data['game']['word'] = choice()
    return context.chat_data['game']['word']


@requires_game_running
def is_true(word: str, context: CallbackContext) -> bool:
    if context.chat_data['game']['word'] == word.lower():
        end_game(context)
        return True
    return False


def end_game(context: CallbackContext) -> bool:
    if 'game' in context.chat_data:
        try:
            del context.chat_data['game']
            return True
        except Exception as e:
            raise e

    return False
