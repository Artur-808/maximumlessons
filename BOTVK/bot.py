import vk_api
import time
import random
from cource import *
from weather import *

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
token = "a17bd94e57b9dcc52e694bb384de090166947eabe70dbdc12e472125888c7089b866ba5917a9e0e7d34b7"
vk = vk_api.VkApi(token=token)
vk._auth_token()
def keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button("курс", color= VkKeyboardColor.PRIMARY)
    keyboard.add_button("погода", color= VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("команды", color=VkKeyboardColor.DEFAULT)
    keyboard.add_button("мем", color=VkKeyboardColor.DEFAULT)
    return keyboard.get_keyboard()
while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] >=1:
        id = messages['items'][0]['last_message']['from_id']
        random_id = random.randint(1, 9999999999999)
        text = messages['items'][0]['last_message']['text']
        owner_id = 176065522
        first_word = text.split(" ")
        if text.lower() == 'начать':
            vk.method("messages.send", {"peer_id": id, "random_id": random_id, "message": "выбор команды", "keyboard": keyboard()})
        elif text.lower() == 'курс':
            vk.method("messages.send", {"peer_id": id, "random_id": random_id, "message": "1$ стоит " + get_course("R01235") + " рублей\n1€ стоит " + get_course("R01239") + " рублей"})
        elif first_word[0].lower() == 'вероятность':
            number = random.randint(0, 100)
            vk.method("messages.send", {"peer_id": id, "random_id": random_id, "message": text + " - " + str(number) + "%"})
        elif first_word[0].lower() == 'сообщение':

            vk.method("messages.send", {"peer_id": owner_id, "random_id": random_id, "message": "сообщение от vk.com/id" + str(id) + " : " + text[10:]})
        elif first_word[0].lower() == 'ответить':
            if id  ==  owner_id:
                vk.method("messages.send", {"peer_id": first_word[1], "random_id": random_id,
                                            "message": "ответ от администрации: " + text[18:]})
            else:
                vk.method("messages.send", {"peer_id": id, "random_id": random_id, "message": "вы не администратор"})
        elif first_word[0].lower() == 'число':
            x = random.randint(int(first_word[1]), int(first_word[2]))
            vk.method("messages.send", {"peer_id": id, "random_id": random_id, "message": "случайное число- " + str(x)})
        elif text.lower() == 'погода':
            vk.method("messages.send", {"peer_id": id, "random_id": random_id, "message": main("Moscow")})
        elif text.lower() == 'команды':
            vk.method("messages.send", {"peer_id": id, "random_id": random_id,
                                        "message": "полный список команд:\nначать - запустить клавиатуру\nкурс - вывести актуальный курс доллара и евро\nвероятность [любое событие]- сгенерировать вероятность любого события\nсообщение [текст]- отправить сообщение администрации\nчисло [1 число] [2 число]- выбрать число в заданном промежутке\nпогода- отобразить погоду на данный момент (Москва)"})
        else:
            vk.method("messages.send", {"peer_id": id, "random_id": random_id, "message": "команда не распознана, для получения списка команд- введите 'команды' "})
