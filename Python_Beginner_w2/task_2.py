#positive(), negative() и zero() должны предшествовать test(). Если этого не будет,
#то будет возникать ошибка уровня компиляции, которая будет говорить, что соответствующий функции не найдены

def test():
    integer = int(input('Введите целое число: '))

    positive() if integer > 0 else negative() if integer < 0 else zero()

def positive():
    print('Положительное')

def negative():
    print('Отрицательное')

def zero():
    print('Вы ввели 0')

test()
