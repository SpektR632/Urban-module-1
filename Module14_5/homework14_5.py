from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.filters.command import Command
from crud_functions import get_all_products, add_user, is_included
api = '7344213269:AAGgjksD28wW_8oe6bQrDFNeAZ72KWvq8Nw'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    await dp.start_polling(bot)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message(F.text == 'Регистрация')
async def sing_up(message: types.Message, state: FSMContext):
    await message.answer('Введите имя пользователя(только латинский алфавит):')
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    if not is_included(message.text):
        await message.answer('Введите свой email:')
        await state.set_state(RegistrationState.email)
    else:
        await message.answer('Пользователь существует, введите другое имя:')
        await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно')
    await state.clear()



kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить')],
    [KeyboardButton(text='Регистрация')]
    ],
    resize_keyboard=True)

inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
     InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ],
    resize_keyboard=True)

inline_buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Банан', callback_data='product_buying')],
    [InlineKeyboardButton(text='Апельсин', callback_data='product_buying')],
    [InlineKeyboardButton(text='Киви', callback_data='product_buying')],
    [InlineKeyboardButton(text='Авокадо', callback_data='product_buying')]
    ],
    resize_keyboard=True)


file_img = ['banan.png', 'orange.png', 'kiwi.png', 'avokado.png']


@dp.message(F.text == 'Купить')
async def get_buying_list(message):
    for id, product, description, price in get_all_products():
        with open(file_img[id-1], 'rb') as img:
            await message.answer(f'Название: {product} | Описание: {description} | Цена: {price}')
            await message.answer_photo(FSInputFile(file_img[id-1]))
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_buy)


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message(F.text == 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n'
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    await message.answer('Привет, я бот помогающий твоему здоровью!', reply_markup=kb)
    await state.set_state(UserState.age)


@dp.callback_query(F.data == 'calories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
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