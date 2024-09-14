from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

api = 'token'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Рады видеть Вас в нашем боте!')


@dp.message(F.text)
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
