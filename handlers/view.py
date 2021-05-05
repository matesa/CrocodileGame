from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler

from helpers.game import get_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    game = get_game(context)

    if game['host'].id == update.effective_user.id:
        update.callback_query.answer(game['word'], True)
    else:
        update.callback_query.answer('This is not for you.', True)


handler = CallbackQueryHandler(callback, pattern='view')
