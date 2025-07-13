import random

def play_rps(user_choice):
    options = ["камень", "ножницы", "бумага"]
    bot_choice = random.choice(options)
    if user_choice == bot_choice:
        return f"Я тоже выбрал {bot_choice}. Ничья!"
    elif (user_choice == "камень" and bot_choice == "ножницы") or \
         (user_choice == "ножницы" and bot_choice == "бумага") or \
         (user_choice == "бумага" and bot_choice == "камень"):
        return f"Я выбрал {bot_choice}. Ты победил!"
    else:
        return f"Я выбрал {bot_choice}. Я победил!"

