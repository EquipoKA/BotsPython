import json 
import requests

TOKEN = "357116280:AAEpGcgOng5u8betuNUj8c865eFqGX49JGo"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
print(URL)

ID_QAZEKE="391707070"
ID_MOCONINJA="123869263"
ID_GRUPO="-1001099384957"
ID_GRUPO_NONAZI="-158272989"

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

mensajes = ["Hola", "Grupo", "de", "clase"]
for mensaje in mensajes:
    send_message(mensaje, ID_GRUPO)
    