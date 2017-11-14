import re

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging
import funcs, weather, time
import picamera
import os
import sys

authors =[391707070]
h264_video = ".h264"
mp4_video = ".mp4"
camera = picamera.PiCamera()


def authoCam(bot, update, chat_id):
    if (chat_id in authors):
	    camPhoto(bot,update,chat_id)
    else:
		bot.sendMessage('No tienes autoridad sobre esta Raspberry pi 3 unlucky',chat_id)		

def authoVid(bot,update,chat_id):
    if (chat_id in authors):
	    camVideo(bot,update,chat_id)
    else:
		bot.sendMessage('No tienes autoridad sobre esta Raspberry pi 3 unlucky',chat_id)

def camPhoto(bot, update, myd):
    foto = "/tmp/" + (time.strftime("%H:%M:%S-%d-%m-%y")) + ".jpeg"
    camera.capture('%s'% foto)	   
    bot.send_photo(myd, open(foto),time.strftime("Foto tomada en hora y fecha: %H:%M:%S - %d/%m/%y"))


def camVideo(bot, update, myd):
    video = "/tmp/" + (time.strftime("%H%M%S%d%m%y")) + ".h264"
    camera.start_recording('%s'% video)	   
    time.sleep(15)
    camera.stop_recording()
    os.system("MP4Box -add "+ video + " " + video + mp4_video)
#    os.system("rm " + video)
    footage = video + mp4_video
    bot.send_video(myd, open(footage),time.strftime("Video grabado en hora y fecha: %H:%M:%S - %d/%m/%y"))


