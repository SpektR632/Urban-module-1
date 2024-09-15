from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


api = 'token'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    await dp.start_polling(bot)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(F.text == 'Calories')
async def all_messages(message: types.Message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    print(data)
    await state.set_state(UserState.weight)
    await message.answer(
        f'Норма калорий для мужчин: {str((10 * int(data['weight']) + 6.25 * int(data['growth'])
                                          - 5 * int(data['age']) + 5))}')
    await message.answer(
        f'Норма калорий для женщин: {str((10 * int(data['weight']) + 6.25 * int(data['growth'])
                                          - 5 * int(data['age']) - 161))}')
    await state.clear()


if __name__ == '__main__':
    asyncio.run(main())
