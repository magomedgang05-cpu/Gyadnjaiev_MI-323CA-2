phone_book = {
    'Заур кызы': '+7-652-743-1235',
    'Степан Б': '+7-937-124-3660',
    'Амир крипс': '+7-553-814-8231'
}

while True:
    print("\n" + "="*30)
    print("Телефонная книга")
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    
    choice = input("Выберите действие (1-4): ")

    if choice == '1':
        print("\nВсе контакты:")
        if phone_book:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("Телефонная книга пуста")
    
    elif choice == '2':
        name = input("Введите имя контакта: ")
        if name in phone_book:
            print(f"Контакт с именем '{name}' уже существует!")
        else:
            phone = input("Введите номер телефона: ")
            phone_book[name] = phone
            print(f"Контакт '{name}' успешно добавлен!")
    
    elif choice == '3':
        name = input("Введите имя контакта для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Контакт '{name}' успешно удалён!")
        else:
            print(f"Контакт с именем '{name}' не найден!")
    
    elif choice == '4':
        print("До свидания!")
        exit()
    
    else:
        print("Неверный выбор! Пожалуйста, выберите от 1 до 4")