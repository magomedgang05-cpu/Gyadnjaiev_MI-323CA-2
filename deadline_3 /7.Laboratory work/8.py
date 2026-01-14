class SnakeCaseMeta(type):
    def __new__(mcs, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                if any(char.isupper() for char in attr_name):
                    raise TypeError(f"Метод '{attr_name}' должен быть написан в snake_case!")
        
        return super().__new__(mcs, name, bases, dct)


try:
    class GoodCode(metaclass=SnakeCaseMeta):
        def get_data(self):
            pass
        
        def calculate_sum(self):
            pass
        
        def process_items(self):
            pass
    
    print("+ GoodCode создан успешно")
    
except TypeError as e:
    print(f"- Ошибка в GoodCode: {e}")


try:
    class BadCode(metaclass=SnakeCaseMeta):
        def GetData(self):
            pass
        
        def ProcessItems(self):
            pass
        
        def __init__(self):
            pass
        
        def __str__(self):
            return "BadCode"
    
    print("- BadCode создан (это не должно было произойти)")
    
except TypeError as e:
    print(f"+ BadCode: {e}")


try:
    class MixedCode(metaclass=SnakeCaseMeta):
        def good_method(self):
            pass
        
        def BadMethod(self):
            pass
        
        def AnotherBadMethod(self):
            pass
    
    print("- MixedCode создан (это не должно было произойти)")
    
except TypeError as e:
    print(f"+ MixedCode: {e}")


try:
    class WithMagicMethods(metaclass=SnakeCaseMeta):
        def __init__(self):
            self.value = 10
        
        def __str__(self):
            return f"Value: {self.value}"
        
        def __getitem__(self, key):
            return key * 2
        
        def get_value(self):
            return self.value
        
        def SetValue(self, value):
            self.value = value
    
    print("- WithMagicMethods создан (это не должно было произойти)")
    
except TypeError as e:
    print(f"+ WithMagicMethods: {e}")