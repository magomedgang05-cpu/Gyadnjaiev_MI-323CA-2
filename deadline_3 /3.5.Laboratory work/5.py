import sys

def create_list(n):
    return [i**2 for i in range(n)]

def create_gen(n):
    return (i**2 for i in range(n))
    
def main():
    n = 1000000
    
    print("Сравнение потребления памяти: список vs генератор")
    print("=" * 60)
    print(f"Количество элементов: {n:,}")
    print()
    
    print("1. СОЗДАНИЕ СПИСКА (create_list):")
    lst = create_list(n)
    lst_size = sys.getsizeof(lst)
    print(f"   Размер списка: {lst_size:,} байт")
    print(f"   Это примерно {lst_size / 1024 / 1024:.2f} МБ")
    
    if len(lst) > 0:
        print(f"   Первый элемент: {lst[0]}")
        print(f"   Последний элемент: {lst[-1]}")
    print()
    
    print("2. СОЗДАНИЕ ГЕНЕРАТОРА (create_gen):")
    gen = create_gen(n)
    gen_size = sys.getsizeof(gen)
    print(f"   Размер генератора: {gen_size:,} байт")
    print(f"   Это примерно {gen_size / 1024:.2f} КБ")
    

    print("   Пример использования генератора:")
    first_values = []
    count = 0
    for value in gen:
        first_values.append(value)
        count += 1
        if count >= 5:
            break
    
    print(f"   Первые 5 значений: {first_values}")
    print(f"   Всего элементов в генераторе: {n:,}")
    print()
    
    print("=" * 60)
    print("СРАВНЕНИЕ:")
    print(f"Список занимает:   {lst_size:,} байт")
    print(f"Генератор занимает: {gen_size:,} байт")
    print()
    
    if lst_size > gen_size:
        ratio = lst_size / gen_size
        print(f"Генератор эффективнее по памяти в {ratio:,.0f} раз!")
    else:
        print("Генератор неожиданно занимает больше памяти!")
    print()
    
    print("АНАЛИЗ СЛОЖНОСТИ ПО ПАМЯТИ (Space Complexity):")
    print("=" * 60)
    print("1. СПИСОК (create_list): O(n) - линейная сложность")
    print("   - Хранит ВСЕ элементы одновременно в памяти")
    print("   - Каждый элемент занимает место (в Python ~28-32 байта на int)")
    print(f"   - Для {n:,} элементов это примерно {n * 28:,} байт")
    print()
    print("2. ГЕНЕРАТОР (create_gen): O(1) - константная сложность")
    print("   - Хранит только состояние итерации, не все элементы")
    print("   - Генерирует значения на лету при каждом обращении")
    print("   - Потребление памяти не зависит от n")
    print()
    
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ НА РАЗНЫХ РАЗМЕРАХ ДАННЫХ:")
    
    sizes = [100, 1000, 10000, 100000, 1000000]
    
    print("\nРазмер (n) | Список (байт) | Генератор (байт) | Отношение")
    print("-" * 60)
    
    for size in sizes:
        lst_test = create_list(size)
        lst_size_test = sys.getsizeof(lst_test)
        
        gen_test = create_gen(size)
        gen_size_test = sys.getsizeof(gen_test)
        
        ratio_test = lst_size_test / gen_size_test if gen_size_test > 0 else float('inf')
        
        print(f"{size:10,} | {lst_size_test:12,} | {gen_size_test:15,} | {ratio_test:8.0f}x")

if __name__ == "__main__":
    main()