from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup
from config import BOT_TOKEN
import asyncio

# Импортируем новые функции
from apps.guess_the_number import play_guess_game
from apps.calculator import calculate_expression
from apps.loan_calculator import calculate_loan
from apps.rock_paper_scissors import play_rps

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🎮 Угадай число"), types.KeyboardButton(text="🧮 Калькулятор")],
            [types.KeyboardButton(text="📄 Кредитный калькулятор"), types.KeyboardButton(text="✂️ Камень-ножницы-бумага")]
        ],
        resize_keyboard=True
    )
    await message.answer("Привет! 👋 Выбери одно из меню:", reply_markup=keyboard)

# Угадай число
@dp.message(lambda m: m.text == "🎮 Угадай число")
async def guess_number_start(message: types.Message):
    await message.answer("Я загадал число от 1 до 100. Напиши число:")

@dp.message(lambda m: m.text.isdigit())
async def guess_number_play(message: types.Message):
    user_number = int(message.text)
    response = play_guess_game(user_number)
    await message.answer(response)

is_waiting_calc = False

@dp.message(lambda m: m.text == "🧮 Калькулятор")
async def calculator_start(message: types.Message):
    global is_waiting_calc
    is_waiting_calc = True
    await message.answer("Введите выражение для вычисления (пример: 2+2):")

@dp.message(lambda m: is_waiting_calc)
async def calculator_compute(message: types.Message):
    global is_waiting_calc
    result = calculate_expression(message.text)
    await message.answer(result)
    is_waiting_calc = False

# Кредитный калькулятор
@dp.message(lambda m: m.text == "📄 Кредитный калькулятор")
async def credit_start(message: types.Message):
    await message.answer("Введите сумму, месяцев и ставку (пример: 100000 12 14.5):")

@dp.message(lambda m: len(m.text.split()) == 3 and all(part.replace('.', '', 1).isdigit() for part in m.text.split()))
async def credit_compute(message: types.Message):
    result = calculate_loan(message.text)
    await message.answer(result)

# Камень-ножницы-бумага
@dp.message(lambda m: m.text == "✂️ Камень-ножницы-бумага")
async def rps_start(message: types.Message):
    await message.answer("Выбери: камень, ножницы или бумага.")

@dp.message(lambda m: m.text.lower() in ["камень", "ножницы", "бумага"])
async def rps_play(message: types.Message):
    result = play_rps(message.text.lower())
    await message.answer(result)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
