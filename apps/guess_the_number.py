import random

class GuessTheNumberGame:
    def __init__(self):
        self.secret = None
        self.is_active = False

    def start_game(self):
        self.secret = random.randint(0, 100)
        self.is_active = True

    def check_guess(self, guess):
        if not guess.isdigit():
            return "Введите число!"
        guess = int(guess)
        if guess == self.secret:
            self.is_active = False
            return "🎉 Поздравляем! Вы угадали!"
        elif guess < self.secret:
            return "🔼 Больше!"
        else:
            return "🔽 Меньше!"
