import random

def play_guess_game(user_number):
    hidden = random.randint(1, 100)
    if user_number == hidden:
        return f"Ты угадал! 🎉 Я тоже загадал {hidden}"
    else:
        return f"Не угадал! Я загадал {hidden}"
