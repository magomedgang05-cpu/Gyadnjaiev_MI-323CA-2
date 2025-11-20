import time

def timer(func):
    """
    Декоратор, который измеряет и выводит время выполнения функции.
    
    Args:
        func: Функция для измерения времени выполнения
        
    Returns:
        function: Обернутая функция с таймером
    """
    def wrapper(*args, **kwargs):
        # Засекаем время начала выполнения
        start_time = time.time()
        
        # Вызываем оригинальную функцию
        result = func(*args, **kwargs)
        
        # Засекаем время окончания и вычисляем разницу
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Выводим время выполнения
        print(f"Время выполнения функции {func.__name__}: {execution_time:.4f} сек")
        
        return result
    
    return wrapper

# Применение декоратора
@timer
def slow_func():
    # имитация долгой работы
    for _ in range(10000000):
        pass

# Пример использования
slow_func()