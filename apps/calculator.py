def calculate_expression(expression):
    try:
        result = eval(expression)
        return f"Результат: {result}"
    except Exception:
        return "Ошибка в выражении!"
