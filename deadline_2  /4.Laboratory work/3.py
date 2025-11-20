tasks = []

while True:
    print("\n" + "="*30)
    print("To-Do List")
    print("1 - Показать все задачи")
    print("2 - Добавить задачу")
    print("3 - Отметить задачу как выполненную")
    print("4 - Выйти")
    
    choice = input("Выберите действие (1-4): ")
    
    if choice == '1':
        if tasks:
            print("\n Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("\n Задач нет!")
    
    elif choice == '2':
        new_task = input("Введите описание задачи: ")
        tasks.append(new_task)
        print(f"Задача '{new_task}' добавлена!")
    
    elif choice == '3':
        if tasks:
            print("\n Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            
            try:
                task_num = int(input("Какую задачу выполнили? "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Задача '{removed_task}' удалена!")
                else:
                    print("Неверный номер задачи!")
            except ValueError:
                print("Пожалуйста, введите число!")
        else:
            print("Нет задач для удаления!")
    
    elif choice == '4':
        print("До свидания!")
        break
    
    else:
        print("Неверный выбор! Пожалуйста, выберите от 1 до 4")