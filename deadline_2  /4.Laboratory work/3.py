tasks = []

def show_tasks():
    if not tasks:
        print("Список задач пуст!")
    else:
        print("Ваши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Введите описание задачи:").strip()
    if task:
        tasks.append(task)
        print(f'Задача "{task}" добавлена!')
    else:
        print("Задача не может быть пустой!")

def complete_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Введите номер выполненной задачи:"))
            if 1 <= task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)
                print(f'Задача "{completed_task}" удалена!')
            else:
                print("Неверный номер задачи!")
        except ValueError:
            print("Введите число!")

while True:
    print("\n" + "-" * 30)
    print("МЕНЮ")
    print("1 - Показать все задачи")
    print("2 - Добавить задачу")
    print("3 - Отметить задачу как выполненную")
    print("4 - Выйти")
    print("-" * 30)
    
    try:
        choice = int(input("Выберите действие (1-4): "))
        
        if choice == 1:
            show_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор! Введите число от 1 до 4.")
    
    except ValueError:
        print("Ошибка! Введите число.")

print(f"Итоговый список задач: {tasks}")