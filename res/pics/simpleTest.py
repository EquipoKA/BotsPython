import telegram, random, math

bot = telegram.Bot(token='402078197:AAHdxsObm-IL6ko0VSlA8QDNGluPr3kiUAE')

print(bot.get_me())
for i in range (0, 10001):
    numeroRandom = 0
    numeroRandom = int(math.floor(random.uniform(0, 6)))
    print(numeroRandom)
    fotoDoge = 'doge{}.jpg'.format(numeroRandom)
    bot.send_photo(chat_id='-158272989', photo=open(fotoDoge, 'rb'))