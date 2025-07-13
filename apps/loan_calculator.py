def calculate_loan(params):
    try:
        parts = params.split()
        amount = float(parts[0])
        months = int(parts[1])
        rate = float(parts[2])
        monthly = (amount * (rate / 100)) / months + (amount / months)
        return f"Платёж в месяц: {monthly:.2f}"
    except Exception:
        return "Ошибка! Введите так: сумма месяцев ставка (пример: 100000 12 14.5)"
