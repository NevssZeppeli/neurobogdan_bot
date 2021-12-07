import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vktoken import vk_token

vk_session = vk_api.VkApi(token = vk_token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 209137754)


# Здесь личные сообщения группы
def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


# Здесь для чатов
def chat_sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        #чаты
        if event.from_chat:
            id = event.chat_id
            msg = event.object.message['text'].lower()

        if event.from_user:
            id = event.user_id
            msg = event.object.message['text'].lower()


