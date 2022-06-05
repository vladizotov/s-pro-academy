def formatting_text_from_existing_file_to_new_file():
    try:
        name_of_existing_file = input("Введите файл содержимое которого необходимо отформатировать (файл должен находиться в той же директории, что и файл программы): ")
        with open(name_of_existing_file) as existing_file:
            list_of_lines = existing_file.readlines()
    except FileNotFoundError:
        print(f"Файл с именем {name_of_existing_file} не найден. Запустите программу заново, чтобы попробовать еще раз")
        return

    try:
        name_of_new_file = input("Введите название для нового файла в который будет создан и в который будет помещен отформатированный текст: ")
        with open(name_of_new_file, 'w') as new_file:
            counter = 0
            while counter < len(list_of_lines):
                new_file.writelines(f"{counter + 1} : {list_of_lines[counter]}")
                counter += 1
    except OSError: #или какой-то дургой Exception – точно не знаю какой тут нужно использовать, искал вот тут https://docs.python.org/3/library/exceptions.html
        print(f"Название файла {name_of_new_file} не допустимо. Или другая системная ошибка.")
