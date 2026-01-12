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


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Поиграть в доту", 1)
    manager.add_task("Сделать ОАИП", 10)
    manager.show_tasks()