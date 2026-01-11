import time

def fibonacci(n):
    """
    Обычная рекурсивная реализация чисел Фибоначчи.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def tail_fibonacci(n, current=0, next_num=1):
    """
    Хвостовая рекурсивная реализация чисел Фибоначчи.
    Аккумуляторы: current = F(i), next_num = F(i+1)
    """
    if n == 0:
        return current
    if n == 1:
        return next_num
    return tail_fibonacci(n - 1, next_num, current + next_num)


def compare_performance():
    n = 35
    
    print(f"Тестирование для n = {n}\n")
    print("=" * 50)

    print("\n1. Обычная рекурсия:")
    start_time = time.time()
    result1 = fibonacci(n)
    time1 = time.time() - start_time
    
    print(f"   Fibonacci({n}) = {result1}")
    print(f"   Время выполнения: {time1:.6f} секунд")

    print("\n2. Хвостовая рекурсия:")
    start_time = time.time()
    result2 = tail_fibonacci(n)
    time2 = time.time() - start_time
    
    print(f"   Tail Fibonacci({n}) = {result2}")
    print(f"   Время выполнения: {time2:.6f} секунд")
    
    print("\n" + "=" * 50)

    print("\nСравнение:")
    if result1 == result2:
        print(f"✓ Результаты совпадают: {result1}")
    else:
        print(f"✗ Ошибка: результаты не совпадают!")
        print(f"  Обычная: {result1}, Хвостовая: {result2}")

    print(f"\nРазница во времени:")
    if time2 > 0:
        speedup = time1 / time2
        print(f"Хвостовая рекурсия быстрее в {speedup:.2f} раз")
    else:
        print("Хвостовая рекурсия мгновенна!")


if __name__ == "__main__":
    compare_performance()