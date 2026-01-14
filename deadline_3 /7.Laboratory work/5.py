class LoggableMixin:
    def log(self, message):
        print(f"[INFO] {self.__class__.__name__}: {message}")


class Employee(LoggableMixin):
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


from dataclasses import dataclass, field

@dataclass
class Product(LoggableMixin):
    name: str
    price: float = field(repr=False)
    weight: float
    is_available: bool = True
    
    def order_cost(self, quantity):
        return self.price * quantity


if __name__ == "__main__":
    emp = Employee("Manager", 50000)
    emp.log("Сотрудник создан")