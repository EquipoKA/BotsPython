import telegram, random, math

bot = telegram.Bot(token='402078197:AAHdxsObm-IL6ko0VSlA8QDNGluPr3kiUAE')
chat_id='-1001099384957'
print(bot.get_me())
for i in range (0, 2):
    bot.send_voice(chat_id=chat_id, voice=open('bazan_nieee_1.ogg', 'rb'))     