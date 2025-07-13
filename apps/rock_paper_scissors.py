iimport random

print("Привет! Давай сыграем в камень-ножницы-бумага.")

while True:
    user_choice = input("Твой выбор (камень/ножницы/бумага или выход): ").lower()
    if user_choice == "выход":
        print("Пока!")
        break

    if user_choice != "камень" and user_choice != "ножницы" and user_choice != "бумага":
        print("Неверный ввод, попробуй ещё раз.")
        continue

    computer_choice = random.choice(["камень", "ножницы", "бумага"])

    if user_choice == computer_choice:
        print("Ничья!")
    elif user_choice == "камень" and computer_choice == "ножницы":
        print("Ты выиграл!")
    elif user_choice == "ножницы" and computer_choice == "бумага":
        print("Ты выиграл!")
    elif user_choice == "бумага" and computer_choice == "камень":
        print("Ты выиграл!")
    else:
        print("Ты проиграл!")
