import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vktoken import vk_token

vk_session = vk_api.VkApi(token = vk_token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 209137754)


# Здесь для чатов
def chat_sender(id, text):
    vk_session.method('messages.send',
                      {'chat_id': id,
                       'message': text,
                       'random_id': 0
                       })


def photo_sender(id, url):
    vk_session.method('messages.send',
                      {'chat_id': id,
                       'attachment': url,
                       'random_id': 0
                       })


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        # чаты
        if event.from_chat:
            chat_id = event.chat_id
            msg = event.object.message['text'].lower()
            if msg[0:3] == '/nb':
                # просто для себя в консоль вывожу
                print(msg)

        # личные сообщения
        if event.from_user:
            user_id = event.user_id
            msg = event.object.message['text'].lower()
            if msg[0:3] == '/nb':
                print(msg)


