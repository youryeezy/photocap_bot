import aiohttp
import os

import requests
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from bs4 import BeautifulSoup

from create_bot import bot

PHOTOS_FOLDER = r"C:\Users\Admin\photo"
DOWNLOAD_FOLDER = os.path.join(PHOTOS_FOLDER, 'downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

start_router = Router()
URL = "https://gekkk.co/929c57a3645c26f885383a354c2f019c"

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')


@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')


@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
    await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')


@start_router.message(F.text == '/get_photos')
async def cmd_get_photos(message: Message):
    await message.answer('Запуск сообщения по команде /get_photos!')

    photo_path = os.path.join(PHOTOS_FOLDER, '2.jpg')
    if not os.path.exists(photo_path):
        await message.answer("Фотография не найдена.")
        return

    photo = FSInputFile(photo_path, filename='2.jpg')
    await message.bot.send_photo(chat_id=message.chat.id, photo=photo)


@start_router.message(F.text.startswith('/download_html'))
async def cmd_download_html(message: Message):

    URL = "https://gekkk.co/929c57a3645c26f885383a354c2f019c"
    if not URL:
        await message.answer("Пожалуйста, предоставьте URL для скачивания HTML файла.")
        return

    async with aiohttp.ClientSession() as session:
        try:
            file_path = await download_html_file(URL, session)
            if file_path:
                await message.answer(f"HTML файл успешно скачан: {file_path}")
                file = FSInputFile(file_path)
                await message.bot.send_document(chat_id=message.chat.id, document=file)
        except Exception as e:
            await message.answer(f"Произошла ошибка при скачивании файла: {str(e)}")


async def download_html_file(url: str, session: aiohttp.ClientSession) -> str:
    filename = "downloaded_page.html"
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)

    async with session.get(url) as response:
        if response.status == 200:
            content = await response.text()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(77)
            return file_path
        else:
            raise Exception(f"Не удалось скачать файл. HTTP статус: {response.status}")


@start_router.message(F.text.startswith('/get_images'))
async def cmd_get_images(message: Message):
    if not URL:
        await message.answer("Пожалуйста, предоставьте URL страницы.")
        return

    try:
        img_paths = download_images_from_url(URL)
        if img_paths:
            await message.answer(f"Найдено {len(img_paths)} картинок. Отправляю их вам...")
            media = [InputMediaPhoto(FSInputFile(img_path)) for img_path in img_paths[:10]]  # Максимум 10 изображений
            await message.bot.send_media_group(chat_id=message.chat.id, media=media)
    except Exception as e:
        await message.answer(f"Произошла ошибка при скачивании картинок: {str(e)}")


def download_images_from_url(url: str) -> list:
    response = requests.get(url)
    response.raise_for_status()  # Проверяет успешность запроса
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')
    if not img_tags:
        raise Exception("Картинки на странице не найдены.")

    img_paths = []
    for i, img_tag in enumerate(img_tags, start=1):
        img_url = img_tag['src']


        img_url = f"https://gekkk.co/{img_url}"
        print(img_url)
        img_response = requests.get(img_url)
        img_response.raise_for_status()

        img_filename = f"downloaded_image_{i}.jpg"
        img_path = os.path.join(DOWNLOAD_FOLDER, img_filename)
        with open(img_path, 'wb') as f:
            f.write(img_response.content)

        img_paths.append(img_path)

    return img_paths