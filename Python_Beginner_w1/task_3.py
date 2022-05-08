number_of_numbers_to_input = 8

print("Программа написана для определения суммы, минимального и максимального значения, "
      f"среди {number_of_numbers_to_input} введенных чисел с клавиатуры\n")

current_input = 1
numbers = []

while current_input <= number_of_numbers_to_input:
    numbers.append(float(input(f"Введите {current_input}е число: ")))
    current_input += 1

print(f"\nСумма введенных чисел равна {sum(numbers)}")
print(f"Максимальное введенное число {max(numbers)}")
print(f"Минимальное введенное число {min(numbers)}")