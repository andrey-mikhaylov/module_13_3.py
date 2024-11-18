from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

try:
    from credentials import token
except ImportError:
    print("Error: You must use your own Telegram Bot API token to use this program")
    print("Place token in credentials.py")
    exit(1)


bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    """ обработчик команды start """
    # печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' .
    # Запускается только когда написана команда '/start' в чате с ботом.
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message):
    """ обработчик остальных сообщений """
    # печатает строку в консоли 'Введите команду /start, чтобы начать общение.'.
    # Запускается при любом обращении не описанном ранее.
    await message.answer('Введите команду /start, чтобы начать общение.')


def main():
    executor.start_polling(dp, skip_updates=True)
    """
    Ввод в чат Telegram:
    Хэй!
    /start
    Вывод в консоль:
    Updates were skipped successfully.
    Введите команду /start, чтобы начать общение.
    Привет! Я бот помогающий твоему здоровью.
    """


if __name__ == '__main__':
    main()


"""
2024/01/19 00:00|Домашнее задание по теме "Методы отправки сообщений".
Цель: написать простейшего телеграм-бота, используя асинхронные функции.

Задача "Он мне ответил!":
Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
Запустите ваш Telegram-бот и проверьте его на работоспособность.
Пример результата выполнения программы:

Примечания:
Для ответа на сообщение запускайте метод answer асинхронно.
При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!
Файл module_13_3.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""