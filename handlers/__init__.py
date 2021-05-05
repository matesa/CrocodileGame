from telegram.ext import Dispatcher

from . import abort
from . import host
from . import message
from . import next
from . import scores
from . import start
from . import view


def add_handlers(dp: Dispatcher):
    dp.add_handler(abort.handler)
    dp.add_handler(host.handler)
    dp.add_handler(message.handler)
    dp.add_handler(next.handler)
    dp.add_handler(scores.handler)
    dp.add_handler(start.handler)
    dp.add_handler(view.handler)
