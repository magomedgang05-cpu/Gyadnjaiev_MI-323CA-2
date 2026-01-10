text = input("Введите произвольный текст:").strip()

replace_input = input("Введите две строчки через пробел:").strip()

replace_parts = replace_input.split()

if len(replace_parts) >= 2:
    old_str = replace_parts[0]
    new_str = replace_parts[1]
    
    formatted_text = text.replace(old_str, new_str)

    print("Отформатированыц текст:")
    print(formatted_text)
else:
    print("Ошибка: нужно ввести две строки через пробел")