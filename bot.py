from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage


from config import settings
import handlers.start
from keyboards import get_keyboard_not_send_notification
from services.history_messages import add_history_message_user
from grpc_python.photocap_pb2 import Message


class ExternalBot:
    def __init__(self):
        self.bot = Bot(settings.bot_token)
        self.dp = self.__settings_dispatcher()



    async def send_message(self, input_data: Message) -> None:
        self.bot.send_message()

    async def start_bot(self) -> None:
        await self.dp.start_polling(self.bot)


external_bot = ExternalBot()