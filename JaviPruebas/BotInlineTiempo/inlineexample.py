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
import picamera
import time

camera = picamera.PiCamera()
simb1 = "%"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
authors =[391707070]

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
    update.message.reply_text('La humedad es del --> %.0f %s '% (mensaje2 , simb1))
   # mensaje3 = handle('clouds')
   # update.message.reply_text('El cielo esta --> %s' % mensaje3)

def authoCam(bot, update):
	chat_id = update.message.chat_id
	for i in range(len(authors)):
		if(chat_id==authors[i]):
			menuCam(bot,update)
		else:
			update.message.reply_text('No tienes autoridad sobre esta Raspberry pi 3 unlucky')		

def menuCam(bot, update):
    mytime = 5
    chat_id = update.message.chat_id
    update.message.reply_text('Elige foto o video')
    if(update.message.text == 'foto'):
        camPhoto(bot,update,chat_id)
    elif (update.message.text == 'video'):
        update.message.reply_text('Elige duracion del video en segundos')
        mytime = update.message.text
        camVideo(bot,update,chat_id,mytime)
        pass    

def camPhoto(bot, update, myd):
    foto = "/tmp/" + (time.strftime("%H:%M:%S-%d/%m/%y")) + ".jpeg"
    camera.capture('%s'% foto)
    bot.send_photo(myd, open(foto),time.strftime("Foto tomada en hora y fecha: %H:%M:%S - %d/%m/%y"))

def camVideo(bot, update, myd, mytime):
    video = "/tmp/" + (time.strftime("%H:%M:%S-%d/%m/%y")) + ".h264"
    camera.start_recording('%s'% video)
    time.sleep(mytime)
    camera.stop_recording()
    bot.send_video(myd, open(video),time.strftime("Video grabado en hora y fecha: %H:%M:%S - %d/%m/%y"))

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('402078197:AAHdxsObm-IL6ko0VSlA8QDNGluPr3kiUAE')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("tempTest", tempTest))
    dp.add_handler(CommandHandler("cameraTest", authoCam))
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
   # if(entry == 'clouds'):
   #     print(weather.getCloudsZaragoza())
   #     return weather.getCloudsZaragoza()
    else:
        return funcs.say()

if __name__ == '__main__':
    main()
