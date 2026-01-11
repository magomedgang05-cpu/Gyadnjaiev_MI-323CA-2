import time
import random

def find_duplicates_quadratic(arr):
    """
    Поиск дубликатов с помощью двух вложенных циклов.
    Сложность: O(n²) - квадратичная.
    """
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

def generate_random_list(size, min_val=1, max_val=100):
    """
    Генерация списка случайных чисел.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]

def main():
    print("Демонстрация разницы между O(n) и O(n²)")
    print("=" * 50)
    
    # Тестируем на списке из 5000 элементов
    print("\n1. Тест с 5000 элементами:")
    list_5000 = generate_random_list(5000, 1, 100)
    
    start_time = time.time()
    duplicates_5000 = find_duplicates_quadratic(list_5000)
    time_5000 = time.time() - start_time
    
    print(f"   Время выполнения: {time_5000:.2f} секунд")
    print(f"   Найдено дубликатов: {len(duplicates_5000)}")
    
    # Тестируем на списке из 10000 элементов
    print("\n2. Тест с 10000 элементами (в 2 раза больше):")
    list_10000 = generate_random_list(10000, 1, 100)
    
    start_time = time.time()
    duplicates_10000 = find_duplicates_quadratic(list_10000)
    time_10000 = time.time() - start_time
    
    print(f"   Время выполнения: {time_10000:.2f} секунд")
    print(f"   Найдено дубликатов: {len(duplicates_10000)}")
    
    # Анализ результатов
    print("\n" + "=" * 50)
    print("АНАЛИЗ РЕЗУЛЬТАТОВ:")
    print(f"Размер данных увеличился в: {10000 / 5000:.1f} раза")
    print(f"Время выполнения увеличилось в: {time_10000 / time_5000:.2f} раза")
    print()
    
    # Теоретическая оценка
    print("ТЕОРЕТИЧЕСКАЯ ОЦЕНКА:")
    print("Для алгоритма O(n²):")
    print(f"   Если n увеличивается в {10000/5000:.1f} раза,")
    print(f"   то время должно увеличиться в {(10000/5000)**2:.1f} раза")
    print()
    
    # Вопрос и ответ
    print("ОТВЕТ НА ВОПРОС:")
    print("Если данные выросли в 2 раза, то время выполнения алгоритма O(n²)")
    print(f"выросло примерно в {time_10000/time_5000:.2f} раза.")
    print()
    print("Эксперимент подтверждает теорию: при увеличении размера данных")
    print("в 2 раза, время выполнения алгоритма O(n²) увеличивается примерно")
    print("в 4 раза (2² = 4), что соответствует квадратичной сложности.")
    
    # Дополнительный пример с оптимизированным алгоритмом
    print("\n" + "=" * 50)
    print("ДЛЯ СРАВНЕНИЯ: как можно ускорить поиск дубликатов?")
    print("Алгоритм с использованием множества (set): O(n)")
    
    def find_duplicates_linear(arr):
        """
        Оптимизированный поиск дубликатов.
        Сложность: O(n) - линейная.
        """
        seen = set()
        duplicates = set()
        for item in arr:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        return list(duplicates)
    
    # Тест оптимизированной версии
    print("\nТест оптимизированного алгоритма (O(n)) на 10000 элементов:")
    start_time = time.time()
    duplicates_linear = find_duplicates_linear(list_10000)
    time_linear = time.time() - start_time
    
    print(f"   Время выполнения: {time_linear:.6f} секунд")
    print(f"   Ускорение по сравнению с O(n²): {time_10000/time_linear:.0f} раз!")
    print(f"   Найдено дубликатов: {len(duplicates_linear)}")

if __name__ == "__main__":
    main()