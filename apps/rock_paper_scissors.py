import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["камень", "ножницы", "бумага"]

    def play(self, user_choice):
        bot_choice = random.choice(self.choices)
        if user_choice == bot_choice:
            return f"🤝 Ничья! Я тоже выбрал {bot_choice}"
        elif (user_choice == "камень" and bot_choice == "ножницы") or \
             (user_choice == "ножницы" and bot_choice == "бумага") or \
             (user_choice == "бумага" and bot_choice == "камень"):
            return f"🎉 Вы победили! Я выбрал {bot_choice}"
        else:
            return f"😢 Вы проиграли! Я выбрал {bot_choice}"
