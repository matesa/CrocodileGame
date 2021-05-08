from telegram.ext import Defaults
from telegram.ext import Updater

from config import BOT_TOKEN
from config import SUDO_USERS

updater = Updater(
    token=BOT_TOKEN,
    defaults=Defaults(
        parse_mode='HTML',
        disable_web_page_preview=True,
        quote=False,
        run_async=True,
    ),
)

dp = updater.dispatcher


if __name__ == '__main__':
    import os
    import sys
    from threading import Thread

    from telegram import Update
    from telegram.ext import CallbackContext, CommandHandler

    from handlers import add_handlers
    from helpers.filters import sudo_only

    if '-r' in sys.argv:
        for user in SUDO_USERS:
            updater.bot.send_message(user, 'Restarted.')

    def stop_and_restart(chat, msg):
        updater.stop()
        os.execl(
            sys.executable,
            sys.executable,
            *sys.argv,
            '-r',
            f'{chat}_{msg}',
        )

    def restart(update: Update, context: CallbackContext):
        update.effective_message.reply_text('Restarting...')
        Thread(
            target=stop_and_restart, args=(
                update.effective_chat.id,
                update.effective_message.message_id,
            ),
        ).start()

    dp.add_handler(CommandHandler('r', restart, sudo_only))
    add_handlers(dp)

    updater.start_polling(drop_pending_updates=True)
    updater.idle()
