print("Программа написана для определения большего из двух введенных чисел с клавиатуры. "
      "Если вы хотите указать дробное число, для разделителя используйте точку.\n")

first_operand = float(input("Введите первое число: "))
second_operand = float(input("Введите второе число: "))

if first_operand > second_operand:
    print(True)
elif first_operand == second_operand:
    print("В задании не указано как обрабатывать такой кейс")
else:
    print(False)