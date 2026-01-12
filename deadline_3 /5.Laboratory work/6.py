class Task:
    def __init__(self, description: str, priority: int):
        self.description = description
        self.priority = priority


class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description: str, priority: int) -> None:
        new_task = Task(description, priority)
        self.tasks.append(new_task)
    
    def show_tasks(self) -> None:
        for task in self.tasks:
            print(f"{task.description} - {task.priority}")
    
    def get_high_priority_tasks(self, min_priority: int) -> list:
        high_priority_tasks = []
        for task in self.tasks:
            if task.priority >= min_priority:
                high_priority_tasks.append(task)
        return high_priority_tasks


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Поиграть в доту", 1)
    manager.add_task("Сделать ОАИП", 10)
    manager.add_task("Позвонить Зауру", 5)
    manager.add_task("Починить шкаф", 3)
    manager.add_task("Сделать отчёт по парктике", 8)
    
    print("Все задачи:")
    manager.show_tasks()
    
    print("\nВажные задачи (приоритет 5+):")
    important_tasks = manager.get_high_priority_tasks(5)
    for task in important_tasks:
        print(task.description)
    
    print("\nСрочные задачи (приоритет 8+):")
    urgent_tasks = manager.get_high_priority_tasks(8)
    for task in urgent_tasks:
        print(f"{task.description} (приоритет: {task.priority})")