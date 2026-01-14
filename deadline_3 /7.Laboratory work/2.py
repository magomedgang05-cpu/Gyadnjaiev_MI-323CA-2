class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Ошибка! Зарплата не может быть отрицательной.")
        else:
            self._salary = value


if __name__ == "__main__":
    emp = Employee("John", 50000)
    emp.salary = -100  # Ошибка!
    emp.salary = 60000  # Успешно
    print(emp.salary)  # 60000