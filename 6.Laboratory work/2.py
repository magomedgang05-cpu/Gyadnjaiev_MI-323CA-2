text = input("Введите произвольный текст: ")

replace_input = input("Введите две строки для замены (строка1 строка2): ")

strings = replace_input.split()

if len(strings) == 2:
    string1, string2 = strings
    
    formatted_text = text.replace(string1, string2)
    
    print("\n Отформатированный текст:")
    print(formatted_text)
else:
    print("Ошибка: нужно ввести ровно две строки через пробел!")