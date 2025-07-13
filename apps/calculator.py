print("Простой калькулятор")

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
operation = input("Выберите операцию (+, -, *, /): ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    if operation == "+":
        print("Результат:", num1 + num2)
    elif operation == "-":
        print("Результат:", num1 - num2)
    elif operation == "*":
        print("Результат:", num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print("Результат:", num1 / num2)
        else:
            print("На ноль делить нельзя!")
    else:
        print("Неизвестная операция")
else:
    print("Ошибка: нужно ввести числа")
