class CreditCalculatorApp:
    def __init__(self):
        self.awaiting_input = False

    def calculate(self, text):
        try:
            amount, months, rate = map(float, text.split())
            monthly_rate = rate / 12 / 100
            total_payment = amount * (1 + monthly_rate * months)
            monthly_payment = round(total_payment / months, 2)
            return f"💳 Ежемесячный платёж: {monthly_payment}₸"
        except:
            return "❌ Ошибка! Введите данные в формате: сумма месяцев ставка"
