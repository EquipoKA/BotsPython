#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, weather, funcs, camera, pir
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def menu(bot, update):
    ''' Aquí se definen los botones '''
    keyboard = [[InlineKeyboardButton("Vídeo", callback_data='1'),
                 InlineKeyboardButton("Foto", callback_data='2'), InlineKeyboardButton("Tiempo", callback_data='3'), InlineKeyboardButton("Seguridad", callback_data='4')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Elige:', reply_markup=reply_markup)


def button(bot, update):
    ''' Aquí se ejecuta al seleccionar unos de los botones '''
    query = update.callback_query
    choice = "{}".format(query.data) # Surrender
    handle(bot, update, choice, query)
'''
    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
'''

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def handle(bot, update, choice, query):
    if (choice == '1'):
        bot.edit_message_text(text="Voy a mandarte un vídeo",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
        camera.authoVid(bot,update,query.message.chat_id)                  
    elif (choice == '2'):
            bot.edit_message_text(text="Voy a mandarte una foto",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
            camera.authoCam(bot,update,query.message.chat_id)

    elif (choice == '3'):
            bot.edit_message_text(text="Conectando a la atmosfera...",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
            tempBot(bot, update, query)
       
    elif (choice == '4'):
	    bot.edit_message_text(text="Modo de vigilancia activado",
			  chat_id=query.message.chat_id,
			  message_id=query.message.message_id)
	    pir.pir_mode(bot, update, query.message.chat_id) 

def tempBot(bot, update, query):
    sbt = "%"
    temperatura = handleTemp('temp')
    viento = handleTemp('wind')
    humedad = handleTemp('humidity')


    bot.sendMessage(text="La temperatura es de {0:.2f} ºC".format(temperatura),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id)

    
    bot.sendMessage(text="La velocidad del viento es de {0:.2f} km/h".format(viento),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id)

    
    bot.sendMessage(text="La humedad es del {0:.2f} %".format(humedad),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id)
                        

'''
    bot.edit_message_text('La temperatura es de --> %.2f °C'% mensaje)
    
    bot.edit_message_text('La velocidad del viento es de --> %.2f km/h'% mensaje1)
    
    bot.edit_message_text('La humedad es del --> %.0f %s '% (mensaje2 , sbt))
'''

def handleTemp(entry):
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

def main():
    # TOKEN
    updater = Updater('402078197:AAHdxsObm-IL6ko0VSlA8QDNGluPr3kiUAE')
    updater.dispatcher.add_handler(CommandHandler('options', menu))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
