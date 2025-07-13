print("Кредитный калькулятор")

amount = input("Сумма кредита: ")
months = input("Срок в месяцах: ")
rate = input("Годовая процентная ставка: ")

if amount.isdigit() and months.isdigit() and rate.replace('.', '', 1).isdigit():
    amount = int(amount)
    months = int(months)
    rate = float(rate)

    monthly_rate = rate / 12 / 100
    total_payment = amount * (1 + monthly_rate * months)
    monthly_payment = round(total_payment / months, 2)

    print("Твой ежемесячный платёж:", monthly_payment)
else:
    print("Ошибка ввода данных")
