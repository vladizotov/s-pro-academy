number = 2
degree_from = 0
degree_to = 20

print(f"Программа написана для вывода стпеней числа {number} от {degree_from} до {degree_to}\n")

while degree_from <= degree_to:
    print(number ** degree_from)
    degree_from += 1