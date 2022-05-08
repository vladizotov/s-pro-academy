def stringWithStar():
    input_string = input('Введите что душа желает: ')

    character_limit = 10
    if len(input_string) > character_limit:
        print(f"Введенная строка длиннее {character_limit} символов")
    elif len(input_string) == character_limit:
        print("В условии не описано как обрабатывать такой кейс, но он может быть")
    else:
        string_with_star = input_string + ((character_limit - len(input_string)) * "*")
        print(string_with_star)

def minAndMaxNumbers():
    number_of_numbers_to_enter = 6

    iterator = 0
    numbers = []
    while iterator < number_of_numbers_to_enter:
        numbers.append(round(float(input(f"Введите {iterator + 1}-е число: ")), 2))
        iterator += 1

    iterator = 0
    min_value = 0
    max_value = 0
    while iterator < len(numbers):
        if iterator == 0:
            min_value = numbers[iterator]
            max_value = numbers[iterator]

        if numbers[iterator] < min_value:
            min_value = numbers[iterator]

        if numbers[iterator] > max_value:
            max_value = numbers[iterator]

        iterator += 1


    #не нашел как для целых чисел с помощью какого-то метода добавить 2 знака после запятой, по этому сделал это "искуственно"
    splitted_text_min_value = str(min_value).split(".")
    if len(splitted_text_min_value[1]) < 2:
        print(str(min_value) + "0")
    else:
        print(min_value)

    splitted_text_max_value = str(min_value).split(".")
    if len(splitted_text_max_value[1]) < 2:
        print(str(max_value) + "0")
    else:
        print(max_value)