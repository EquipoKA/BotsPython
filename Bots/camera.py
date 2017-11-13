import re

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging
import funcs, weather, time
import picamera

authors =[391707070]

camera = picamera.PiCamera()


def authoCam(bot, update, chat_id,mess_id):
    if (chat_id in authors):
	    camPhoto(bot,update,chat_id)
    else:
		bot.sendMessage('No tienes autoridad sobre esta Raspberry pi 3 unlucky',chat_id,mess_id)		

def authoVid(bot,update,chat_id):
    if (chat_id in authors):
	    camVideo(bot,update,chat_id)
    else:
		bot.sendMessage('No tienes autoridad sobre esta Raspberry pi 3 unlucky',chat_id,mess_id)

def camPhoto(bot, update, myd):
    foto = "/tmp/" + (time.strftime("%H:%M:%S-%d-%m-%y")) + ".jpeg"
    camera.capture('%s'% foto)	   
    bot.send_photo(myd, open(foto),time.strftime("Foto tomada en hora y fecha: %H:%M:%S - %d/%m/%y"))


def camVideo(bot, update, myd):
    video = "/tmp/" + (time.strftime("%H:%M:%S-%d-%m-%y")) + ".h264"
    camera.start_recording('%s'% video)	   
    time.sleep(5)
    camera.stop_recording()
    bot.send_video(myd, open(video),time.strftime("Foto tomada en hora y fecha: %H:%M:%S - %d/%m/%y"))

