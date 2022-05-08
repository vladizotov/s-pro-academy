def getInput():
    return input('Введите что душа желает: ')

#доступными методами isnumeric() и isdigit() "в лоб" нельзя проверить введенное значение, так как ввод может быть отрицательным,
# то написал следующую функцию для обработки в том числе и отрицательных чисел
def testInput(value):
    value_to_list = list(value)

    #проверка на не ввод занчения (просто нажали Enter)
    if len(value_to_list) == 0:
        return False

    # проверка на то, что если значение состоит из 1 символа, то оно не может быть отрицательным
    if len(value_to_list) == 1:
        if value.isdigit() == True:
            return True
        else:
            return False

    #цикл в котором проверяем введенное значение
    iterator = 0
    while iterator < len(value_to_list):

        #проверка для обратботки отрицательных чисел
        if iterator == 0:
            if value_to_list[iterator] == "-" or value_to_list[iterator].isdigit() == True:
                iterator += 1
                continue
            else:
                return False

        #проверка оставшихся цифр значения
        if value_to_list[iterator].isdigit() == True:
            iterator += 1
            continue
        else:
            return False

    return True
    #по идеи эту функцию можно расширить и для проверки рациональных чисел, добавив проверки на допустимость разделителя в определенных местах

def strToInt(value):
    return int(value)

def printInt(value):
    print(value)

input_value = getInput()
if testInput(input_value):
    output_value = strToInt(input_value)
    printInt(output_value)