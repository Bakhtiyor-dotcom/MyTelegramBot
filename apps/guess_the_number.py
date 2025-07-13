import random

print("Я загадал число от 0 до 100. Попробуй угадать!")

secret = random.randint(0, 100)

guess = input("Введи число: ")

if guess.isdigit():
    guess = int(guess)
    if guess == secret:
        print("Ура! Ты угадал!")
    else:
        print("Не угадал. Было загадано:", secret)
else:
    print("Это не число :(")
