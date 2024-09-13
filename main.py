from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

api = 'token'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command('start')) # Подскажите, как установить две версии python, пришлось пока на 3.12 установить самый свежий aiogram
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
