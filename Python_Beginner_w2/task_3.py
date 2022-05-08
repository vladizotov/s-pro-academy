def concatenation():
    first_string = input('Введите первую часть результирующей строки: ')
    second_string = input('Введите вторую часть результирующей строки: ')
    print(first_string + " " + second_string)

concatenation()

def until_zero_is_entered():
    while True:
        first_operand = float(input(
            f'Введите первое число: '))

        if first_operand == 0:
            break

        second_operand = float(input(
            f'Введите второе число: '))

        if second_operand == 0:
            break

        print(first_operand*second_operand)

until_zero_is_entered()