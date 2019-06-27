import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from memes import get_memes
from cource import *
def main():
    token = "a17bd94e57b9dcc52e694bb384de090166947eabe70dbdc12e472125888c7089b866ba5917a9e0e7d34b7"

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    hello = """ 
    привет, я бот, для получения списка команд, введите 'команды' 
    """
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msgtext= event.text.lower()
            if msgtext == "мем":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), attachment=get_memes("-147286578"))
            elif msgtext == "курс":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="1$ стоит " + get_course("R01235") + " рублей\n1€ стоит " + get_course("R01239") + " рублей")

main()

