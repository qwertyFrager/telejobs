import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message, KeyboardButton, WebAppInfo, FSInputFile
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Если нужно отправлять локальный файл, используйте:
# from aiogram.types import FSInputFile

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
APP_URL = os.getenv("APP_URL")

async def cmd_start(message: Message):
    """
    Хэндлер на команду /start.
    Отправляет одно сообщение с:
     - фото,
     - подписью (text),
     - кнопкой WebApp.
    """

    # 1) Создаём кнопку WebApp
    webapp_button = KeyboardButton(
        text="Открыть мини-приложение",
        web_app=WebAppInfo(url=APP_URL)  # <-- подставьте свой URL
    )

    # 2) Создаём "билдер" клавиатуры и добавляем в него кнопку
    builder = ReplyKeyboardBuilder()
    builder.add(webapp_button)

    # 3) Преобразуем билдер в ReplyKeyboardMarkup
    keyboard = builder.as_markup(resize_keyboard=True)

    # 4) Текст сообщения (будет в виде подписи к фото)
    text_caption = (
        "Добро пожаловать в бота!\n"
        "Нажмите на кнопку ниже, чтобы открыть мини-приложение."
    )

    # 5) Ссылка на картинку (можно использовать любой URL)
    photo = FSInputFile("images/banner.png")

    # Если хотим отправлять фото из локального файла:
    # photo = FSInputFile("images/welcome.jpg")
    # await message.answer_photo(photo=photo, caption=text_caption, reply_markup=keyboard)

    # Отправляем фото по URL, с подписью и клавиатурой
    await message.answer_photo(
        photo=photo,
        caption=text_caption,
        reply_markup=keyboard
    )


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем хэндлер на команду /start
    dp.message.register(cmd_start, Command("start"))

    # Очищаем очередь непрочитанных апдейтов и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
