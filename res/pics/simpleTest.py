import telegram, random, math

bot = telegram.Bot(token='402078197:AAHdxsObm-IL6ko0VSlA8QDNGluPr3kiUAE')
ID=''
print(bot.get_me())
for i in range (0, 11):
    numeroRandom = 0
    numeroRandom = int(math.floor(random.uniform(1, 6)))
    print(numeroRandom)
    fotoDoge = 'doge{}.jpg'.format(numeroRandom)
    bot.send_photo(chat_id=ID, photo=open(fotoDoge, 'rb'))