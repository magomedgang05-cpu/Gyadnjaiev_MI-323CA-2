class Person:
    def __setattr__(self, name, value):
        if name == 'age' and value < 0:
            print("Нельзя быть младше 0")
            value = 0
        super().__setattr__(name, value)
    
    def __getattr__(self, name):
        return None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    p = Person("Ivan", 30)
    p.age = -5
    print(p.age)
    print(p.name)
    print(p.job)
       
    "Доп тестики"
    p.age = -10
    print(f"Возраст после попытки установить -10: {p.age}")
    
    print(f"Несуществующий атрибут 'address': {p.address}")