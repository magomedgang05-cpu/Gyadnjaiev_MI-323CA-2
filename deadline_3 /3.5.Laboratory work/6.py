import time
from typing import List, Optional

def binary_search_recursive(arr: List[int], target: int, low: int = 0, high: Optional[int] = None) -> Optional[int]:
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return None
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

def binary_search_iterative(arr: List[int], target: int) -> Optional[int]:
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

def linear_search(arr: List[int], target: int) -> Optional[int]:
    for i, value in enumerate(arr):
        if value == target:
            return i
    return None

def measure_performance():
    print("Создаем отсортированный список от 0 до 10 000 000:")
    sorted_list = list(range(0, 10000001))
    
    target = -1
    
    print("\n=== ТЕСТ 1: Бинарный поиск (итеративный) ===")
    start_time = time.time()
    result = binary_search_iterative(sorted_list, target)
    binary_time = time.time() - start_time
    print(f"Результат: {'Найден' if result is not None else 'Не найден'}")
    print(f"Время выполнения: {binary_time:.6f} секунд")
    
    print("\n=== ТЕСТ 2: Бинарный поиск (рекурсивный) ===")
    start_time = time.time()
    result = binary_search_recursive(sorted_list, target)
    binary_rec_time = time.time() - start_time
    print(f"Результат: {'Найден' if result is not None else 'Не найден'}")
    print(f"Время выполнения: {binary_rec_time:.6f} секунд")
    
    print("\n=== ТЕСТ 3: Линейный поиск (оператор in) ===")
    start_time = time.time()
    result = target in sorted_list
    linear_in_time = time.time() - start_time
    print(f"Результат: {'Найден' if result else 'Не найден'}")
    print(f"Время выполнения: {linear_in_time:.6f} секунд")
    
    print("\n=== ТЕСТ 4: Линейный поиск (функция) ===")
    start_time = time.time()
    result = linear_search(sorted_list, target)
    linear_func_time = time.time() - start_time
    print(f"Результат: {'Найден' if result is not None else 'Не найден'}")
    print(f"Время выполнения: {linear_func_time:.6f} секунд")
    
    print("\n=== СРАВНЕНИЕ РЕЗУЛЬТАТОВ ===")
    print(f"Бинарный поиск (итеративный): {binary_time:.6f} сек")
    print(f"Бинарный поиск (рекурсивный): {binary_rec_time:.6f} сек")
    print(f"Линейный поиск (оператор in): {linear_in_time:.6f} сек")
    print(f"Линейный поиск (функция):     {linear_func_time:.6f} сек")
    
    if binary_time > 0:
        print(f"\nОтношение времени линейного к бинарному поиску:")
        print(f"Итеративный бинарный поиск быстрее в {linear_in_time / binary_time:.0f} раз")
    
if __name__ == "__main__":
    measure_performance()