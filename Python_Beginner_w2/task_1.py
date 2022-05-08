school = {'1a': 1, '1b': 2, '1c': 3, '2a': 4, '3a': 5, '3b': 6, '4a': 7, '5a': 8, '6a': 9, '6b': 10,
          '7a': 11, '7b': 12, '8a': 13, '9a': 14, '10a': 15, '10b': 16, '11a': 17, '11b': 18} #сделал две вариации значений сета для разнообразия проверок кода ниже
# school = dict.fromkeys(['1a', '1b', '1c', '2a', '3a', '3b', '4a', '5a', '6a', '6b', '7a', '7b', '8a', '9a', '10a', '10b', '11a', '11b'], 27)

class_name_limit_length = 3
exit_from_first_loop = 'exit'

# написал простую логику для пункта изминения количества учащихся с вводом пользователем класса и нового количества с простыми проверками
while True:
    class_in_which_number_of_students_has_changed = input(
        f'Введите название класса для которого необходимо изменить количество учеников: ')

    # чтобы пользователь мог выйти из цикла
    if class_in_which_number_of_students_has_changed == exit_from_first_loop:
        break

    # ограничиваем длинну ввода название класса, так как оно не может содержать более 3 символов
    if len(class_in_which_number_of_students_has_changed) > class_name_limit_length:
        print(f'Название класса не может содержать более {class_name_limit_length} символов, '
              f'попробуйте ввести навание класса еще раз или введите {exit_from_first_loop} для выхода.')
        continue

    # проверка на ввод существующего названия класса
    if school.get(class_in_which_number_of_students_has_changed, 'No such class exists') == 'No such class exists':
        print(f'В системе управления не существует класса "{class_in_which_number_of_students_has_changed}", '
              f'попробуйте ввести навание класса еще раз или введите exit для выхода.')
    else:
        break

minimum_number_of_pupils = 10
maximum_number_of_pupils = 50
exit_from_second_loop = 99

if class_in_which_number_of_students_has_changed != exit_from_first_loop:
    while True:
        new_number_of_pupils = int(input(f'Введите новое количество учеников в классе {class_in_which_number_of_students_has_changed}: '))

        if new_number_of_pupils == exit_from_second_loop:
            break

        # проверка на не ввод "левых" значений
        if new_number_of_pupils > maximum_number_of_pupils or new_number_of_pupils < minimum_number_of_pupils:
            print(f'Введенное вами новое значение для класса "{class_in_which_number_of_students_has_changed}" не может быть меньше {minimum_number_of_pupils} или больше {maximum_number_of_pupils}. '
                f'Измените количество учеников или введите {exit_from_second_loop} для выхода.')
            continue

        # проверка ввод нового отличного от текущего значения
        if school.get(class_in_which_number_of_students_has_changed) == new_number_of_pupils:
            print(f'Введенное вами новое значение для класса "{class_in_which_number_of_students_has_changed}" равно текущему. '
                  f'Возможно вы ошиблись или значение не требует изминения. Измените количество учеников или введите {exit_from_second_loop} для выхода.')
            continue

        # собственно меняем количество
        if school.get(class_in_which_number_of_students_has_changed) != new_number_of_pupils:
            school[class_in_which_number_of_students_has_changed] = new_number_of_pupils
            break

        else:
            break

# добавления нового класса, но уже без ввода пользователем с клавиатуры
new_class = '10b'
if new_class in school:
    print(f'Класс {new_class} уже существет')
else:
    school.setdefault(new_class, 0)

# расформирование класса, но также без ввода пользователем с клавиатуры
disbanded_class = '1b'
if disbanded_class in school:
    del school[disbanded_class]
    print(f'{disbanded_class} класс успешно удален')
else:
    print(f'Класса {disbanded_class} не существет')

# вычесление общего количества учащихся в школе
print(f"Общее количество учеников в школе {sum(school.values())}")

# функция, которую нужно написать в задании
def reverse_dictionary(dictionary):
    # нагуглил эти две строки для получения уникальных значений
    from collections import Counter
    unique_values = Counter(school.values())

    reverse_dict = {}
    temp_list = list(dictionary.items())
    number = 0

    # так как значения в исходном словаре могут совпадать, сделал две логики формирования ключа для нового словаря
    if len(unique_values) != len(dictionary):
        while number < len(dictionary.items()):
            temp_tuple = temp_list[number]
            reverse_dict[f'{temp_tuple[1]}{temp_tuple[0]}'] = temp_tuple[0]
            number += 1
    else:
        while number < len(dictionary.items()):
            temp_tuple = temp_list[number]
            reverse_dict[temp_tuple[1]] = temp_tuple[0]
            number += 1

    return reverse_dict

print(school)
print(reverse_dictionary(school))