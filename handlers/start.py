from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile, FSInputFile
import os
import random
import types
from create_bot import bot
PHOTOS_FOLDER = r"C:\Users\Admin\photo"
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')

@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
    await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')

@start_router.message(F.text =='/get_photos')
async def cmd_get_photos(message: Message):
    await message.answer('Запуск сообщения по команде /get_photos!')
    #photos = os.listdir(PHOTOS_FOLDER)
    #print(photos)
    #if not photos:
    #    await message.answer("В папке нет фотографий.")
    #    return

    #photo_name = random.choice(photos)
    #hoto_path = os.path.join(PHOTOS_FOLDER, photo_name)

    #Отправляем файл, передавая строку с путем к нему
    #photo = open(r"C:\Users\Admin\photo\1.jpg", 'rb')
    #await bot.send_photo(chat_id=message.chat.id, photo=photo)





    photo = FSInputFile(path=r"C:\Users\Admin\photo\2.jpg", filename='2.jpg')

    await message.bot.send_photo(chat_id=message.chat.id, photo=photo)




