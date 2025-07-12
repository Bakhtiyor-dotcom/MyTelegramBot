from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup
from config import BOT_TOKEN
import asyncio

# Импорт мини-приложений
from apps.guess_the_number import GuessTheNumberGame
from apps.calculator import CalculatorApp
from apps.credit_calculator import CreditCalculatorApp
from apps.rock_paper_scissors import RockPaperScissorsGame

# Создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Главное меню
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🎮 Угадай число"), types.KeyboardButton(text="🧮 Калькулятор")],
            [types.KeyboardButton(text="📄 Кредитный калькулятор"), types.KeyboardButton(text="✂️ Камень-ножницы-бумага")]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Привет! 👋 Это бот с мини-приложениями.\nВыбери одно из меню:",
        reply_markup=keyboard
    )

# Угадай число
guess_game = GuessTheNumberGame()

@dp.message(lambda m: m.text == "🎮 Угадай число")
async def guess_number_start(message: types.Message):
    guess_game.start_game()
    await message.answer("Я загадал число от 0 до 100. Попробуй угадать!")

@dp.message(lambda m: guess_game.is_active)
async def guess_number_play(message: types.Message):
    response = guess_game.check_guess(message.text)
    await message.answer(response)

# Калькулятор
calc_app = CalculatorApp()

@dp.message(lambda m: m.text == "🧮 Калькулятор")
async def calculator_start(message: types.Message):
    await message.answer("Введите выражение для калькуляции (например: 2 + 2):")
    calc_app.awaiting_input = True

@dp.message(lambda m: calc_app.awaiting_input)
async def calculator_compute(message: types.Message):
    result = calc_app.calculate(message.text)
    await message.answer(result)
    calc_app.awaiting_input = False

# Кредитный калькулятор
credit_app = CreditCalculatorApp()

@dp.message(lambda m: m.text == "📄 Кредитный калькулятор")
async def credit_start(message: types.Message):
    await message.answer("Введите сумму, месяцев и ставку (пример: 100000 12 14.5):")
    credit_app.awaiting_input = True

@dp.message(lambda m: credit_app.awaiting_input)
async def credit_compute(message: types.Message):
    result = credit_app.calculate(message.text)
    await message.answer(result)
    credit_app.awaiting_input = False

# Камень-ножницы-бумага
rps_game = RockPaperScissorsGame()

@dp.message(lambda m: m.text == "✂️ Камень-ножницы-бумага")
async def rps_start(message: types.Message):
    await message.answer("Выберите: камень, ножницы или бумага.")

@dp.message(lambda m: m.text.lower() in ["камень", "ножницы", "бумага"])
async def rps_play(message: types.Message):
    result = rps_game.play(message.text.lower())
    await message.answer(result)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
