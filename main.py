import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vktoken import vk_token

vk_session = vk_api.VkApi(token = vk_token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 209137754)


def sender(id, text):
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})


def chat_sender(id, text):
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id = event.chat_id
            msg = event.object.message['text'].lower()


