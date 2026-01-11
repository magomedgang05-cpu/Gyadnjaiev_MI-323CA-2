import time
import random

def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

def find_pair_fast(arr, target):
    """
    Оптимизированное решение задачи Two Sum.
    Сложность: O(n) - линейная.
    """
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            return (num, complement)
        seen.add(num)
    
    return None

def generate_test_data(size, min_val=-1000, max_val=1000):
    """
    Генерация тестовых данных.
    Гарантируем, что пара существует.
    """
    arr = [random.randint(min_val, max_val) for _ in range(size)]

    if size >= 2:
        idx1, idx2 = random.sample(range(size), 2)
        num1 = arr[idx1]
        num2 = arr[idx2]
        target = num1 + num2
    else:
        target = random.randint(min_val * 2, max_val * 2)
    
    return arr, target

def main():
    print("Оптимизация задачи Two Sum")
    print("=" * 60)

    size = 10000
    arr, target = generate_test_data(size)
    
    print(f"Размер массива: {size} элементов")
    print(f"Целевая сумма: {target}")
    print()

    print("1. Тестируем МЕДЛЕННОЕ решение (O(n²)):")
    start_time = time.time()
    result_slow = find_pair_slow(arr, target)
    time_slow = time.time() - start_time
    
    if result_slow:
        print(f"   Найдена пара: {result_slow}")
        print(f"   {result_slow[0]} + {result_slow[1]} = {target}")
    else:
        print("   Пара не найдена")
    print(f"   Время выполнения: {time_slow:.6f} секунд")
    print()

    print("2. Тестируем БЫСТРОЕ решение (O(n)):")
    start_time = time.time()
    result_fast = find_pair_fast(arr, target)
    time_fast = time.time() - start_time
    
    if result_fast:
        print(f"   Найдена пара: {result_fast}")
        print(f"   {result_fast[0]} + {result_fast[1]} = {target}")
    else:
        print("   Пара не найдена")
    print(f"   Время выполнения: {time_fast:.6f} секунд")
    print()

    print("=" * 60)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ:")
    print(f"Медленное решение (O(n²)): {time_slow:.6f} сек")
    print(f"Быстрое решение (O(n)):    {time_fast:.6f} сек")
    print()
    
    if time_fast > 0:
        speedup = time_slow / time_fast
        print(f"Быстрое решение быстрее в {speedup:.0f} раз!")
    else:
        print("Быстрое решение работает мгновенно!")
    print()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ НА РАЗНЫХ РАЗМЕРАХ ДАННЫХ:")
    
    sizes = [100, 1000, 5000, 10000]
    
    for test_size in sizes:
        test_arr, test_target = generate_test_data(test_size)

        start = time.time()
        _ = find_pair_slow(test_arr, test_target)
        slow_time = time.time() - start
        
        start = time.time()
        _ = find_pair_fast(test_arr, test_target)
        fast_time = time.time() - start
        
        if fast_time > 0:
            ratio = slow_time / fast_time
        else:
            ratio = float('inf')
        
        print(f"\nРазмер: {test_size} элементов")
        print(f"  O(n²): {slow_time:.6f} сек")
        print(f"  O(n):  {fast_time:.6f} сек")
        print(f"  Ускорение: {ratio:.0f}x")

if __name__ == "__main__":
    main()