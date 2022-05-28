class FormulaError(Exception):
    pass

number_of_expression_elements = 3

def calculator(expression_in_string):
    if len(expression_in_string.split()) != number_of_expression_elements:
        raise FormulaError(f"Выражение должно состоять из {number_of_expression_elements} элементов")

    try:
        first_operand, second_operand = float(expression_in_string.split()[0]), float(expression_in_string.split()[-1])
    except ValueError:
        raise FormulaError("Операнды введенного выражения должны быть числами")

    if expression_in_string.split()[1] == '+':
        return first_operand + second_operand
    elif expression_in_string.split()[1] == '-':
        return first_operand - second_operand
    elif expression_in_string.split()[1] == '*':
        return first_operand * second_operand
    elif expression_in_string.split()[1] == '/':
        return first_operand / second_operand
    else:
        raise FormulaError("Обработка такой математической операции не предусмотрена программой или вы допустили ошибку при вводе")