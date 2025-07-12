class CalculatorApp:
    def __init__(self):
        self.awaiting_input = False

    def calculate(self, expression):
        try:
            result = eval(expression)
            return f"Результат: {result}"
        except:
            return "❌ Ошибка в выражении!"
