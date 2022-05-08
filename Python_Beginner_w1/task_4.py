print("Программа написана для вывода введенной вами строки в том регистре, "
      "букв регистра которого больше в введенной строке\n")

input_string = input("Введите любую произвольную строку : ")

amount_lower = 0
amount_upper = 0

for char in input_string:
    if char.islower():
        amount_lower += 1
    if char.isupper():
        amount_upper += 1

if amount_lower >= amount_upper:
    print(f"В введенной строке больше или равно символов нижнего регистра "
          f"по этому результирующая строка имеет слудующий вид: {input_string.lower()}")
else:
    print(f"В введенной строке больше символов верхнего регистра "
          f"по этому результирующая строка имеет слудующий вид: {input_string.upper()}")