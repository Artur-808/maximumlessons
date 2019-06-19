import telebot
token = "774948520:AAGbpNrtMftNXq0o7_aEMBXsq3i0WRcpD7o"
bot = telebot.TeleBot(token)


def get_last_message():
    return bot.get_updates()[-1]


def text(last_message):
    return last_message.message.text


def get_id(last_message):
    return last_message.message.chat.id

update_id = 0

while True:
    last_messages = get_last_message()
    text_message = text(last_messages).lower()
    ids = get_id(last_messages)
    new_update_id = last_messages.update_id
    if new_update_id != update_id:
        if text_message in ["привет", "hello", "hi"]:
            response = "Привет"
            bot.send_message(chat_id=ids, text=response)
        update_id = new_update_id