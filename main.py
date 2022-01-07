import vk_api

from commands.values import dollar, euro
from commands.anekdots import anekdot
from commands.help import help

from datetime import datetime
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vktoken import vk_token

vk_session = vk_api.VkApi(token=vk_token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 209137754)


def chat_sender(id, text):
    vk_session.method('messages.send',
                      {'chat_id': id,
                       'message': text,
                       'random_id': 0  # вот эта штука вообще не нужна, но ВК требует её наличия в методе :(
                       })


def photo_sender(id, url):
    vk_session.method('messages.send',
                      {'chat_id': id,
                       'attachment': url,
                       'random_id': 0
                       })


# слушаем сервер
print("Бот включился\n")
for event in longpoll.listen():
    # обработка сообщений
    if event.type == VkBotEventType.MESSAGE_NEW:

        # перехватываем сообщения из чата
        if event.from_chat:
            chat_id = event.chat_id
            msg = event.object.message['text'].lower()
            author = event.object.message['from_id']

            if msg[0:3] == '/nb':
                # для себя в консоль вывожу, для отладки
                print("Сообщение в чате", str(chat_id))
                print("Автор", author)
                print(str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print("Текст:", msg)
                print()

                if "помощь" in msg:
                    chat_sender(chat_id, help)
                elif "курс доллара" in msg:
                    chat_sender(chat_id, dollar())
                elif "курс евро" in msg:
                    chat_sender(chat_id, euro())
                elif "анекдот" in msg:
                    chat_sender(chat_id, anekdot())

            # просто проверка отправки фото
            if msg == "f":
                photo_sender(chat_id, "photo-209137754_457239023")

    # если человек вышел
    elif event.type == VkBotEventType.GROUP_LEAVE:
        print("Пользователь покинул чат")
        photo_sender(chat_id, "photo-209137754_457239023")
    # если вошёл
    elif event.type == VkBotEventType.GROUP_JOIN:
        print("Пользователь зашёл в чат")
        photo_sender(chat_id, "doc280209342_617512806")