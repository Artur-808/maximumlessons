import vk_api
from memes import get_memes
from cource import *
from weather import *
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from pictures import *
from vk_api.utils import get_random_id
import time
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
    keyboard.add_line()
    keyboard.add_button("дошик", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("пикча", color=VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()


while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] >=1:
        id = messages['items'][0]['last_message']['from_id']
        text = messages['items'][0]['last_message']['text']
        owner_id = 176065522
        first_word = text.split(" ")
        if text.lower() == 'начать':
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": "выбор команды", "keyboard": keyboard()})
        elif text.lower() == 'курс':
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": "1$ стоит " + get_course("R01235") + " рублей\n1€ стоит " + get_course("R01239") + " рублей"})
        elif first_word[0].lower() == 'вероятность':
            number = random.randint(0, 100)
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": text + " - " + str(number) + "%"})
        elif first_word[0].lower() == 'сообщение':

            vk.method("messages.send", {"peer_id": owner_id, "random_id": get_random_id(), "message": "сообщение от vk.com/id" + str(id) + " : " + text[10:]})
        elif first_word[0].lower() == 'ответить':
            if id  ==  owner_id:
                vk.method("messages.send", {"peer_id": first_word[1], "random_id": get_random_id(),
                                            "message": "ответ от администрации: " + text[18:]})
            else:
                vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": "вы не администратор"})
        elif first_word[0].lower() == 'число':
            x = random.randint(int(first_word[1]), int(first_word[2]))
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": "случайное число- " + str(x)})
        elif text.lower() == 'погода':
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": main("Moscow")})
        elif text.lower() == 'команды':
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(),
                                        "message": """полный список команд:
                                        начать - запустить клавиатуру
                                        курс - вывести актуальный курс доллара и евро
                                        вероятность [любое событие]- сгенерировать вероятность любого события
                                        сообщение [текст]- отправить сообщение администрации
                                        число [1 число] [2 число]- выбрать число в заданном промежутке
                                        погода- отобразить погоду на данный момент (Москва)
                                        мем- получить мем прямиком из 2011
                                        дошик- экспресс таймер для заваривания дошика (во время работы таймера другие команды не работают)
                                        пикча- кидает классную картинку, отличная функция для любителей сохраненок (внимание: функция глючит, не использовать 2 раза, подряд)"""})
        elif text.lower() == 'мем':
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "attachment": get_memes(-158083244)})
        elif text.lower() == 'дошик':
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": "таймер пошел"})
            time.sleep(300)
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": "ваш дошик готов"})
        elif text.lower() == 'пикча':
            groops = [-162232514, -180624147, -168784706, -139278549, -181884082, -182539984]
            group = random.choice(groops)
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "attachment": get_pictures(group)})
        else:
            vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(), "message": "команда не распознана, для получения списка команд- введите 'команды' "})


