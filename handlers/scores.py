from telegram import Update
from telegram.ext import CommandHandler

from helpers.wrappers import nice_errors
from mongo import users


@nice_errors
def callback(update: Update, _):
    total_scores = users.total_scores(update.effective_user.id)
    scores_in_chat = users.scores_in_chat(
        update.effective_chat.id,
        update.effective_user.id,
    ) if (
        update.effective_chat.type == 'supergroup'
    ) else '<code>not in group</code>'

    update.effective_message.reply_text(
        f'Your total scores: {total_scores}\nYour scores in this chat: {scores_in_chat}',
    )


handler = CommandHandler('scores', callback)
