def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами: {args} {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Результат: {result}")
        
        return result
    
    return wrapper

@logger
def add(a, b):
    return a + b

add(5, 10)