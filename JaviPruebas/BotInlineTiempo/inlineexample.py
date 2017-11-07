#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4

import re

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging
import funcs, weather

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(
                query.upper())),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN))]

    update.inline_query.answer(results)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def tempTest(bot, update):
    mensaje = handle('temp')
    update.message.reply_text('La temperatura es de --> %.2f °C'% mensaje)
    mensaje1 = handle('wind')
    update.message.reply_text('La velocidad del viento es de --> %.2f km/h'% mensaje1)
    mensaje2 = handle('humidity')
    update.message.reply_text('La humedad es del --> %f'% mensaje2)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('402078197:AAHdxsObm-IL6ko0VSlA8QDNGluPr3kiUAE')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("tempTest", tempTest))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def handle(entry):
    if (entry == 'temp'):
        print(weather.getTempZaragoza())
        return weather.getTempZaragoza()
    if (entry == 'wind'):
        print(weather.getWindZaragoza())
        return weather.getWindZaragoza()
    if (entry == 'humidity'):
        print(weather.getHumidityZaragoza())
        return weather.getHumidityZaragoza()
    else:
        return funcs.say()

if __name__ == '__main__':
    main()
