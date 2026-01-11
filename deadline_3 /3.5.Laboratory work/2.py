import time

original_list = list(range(100_000))

test_list = original_list.copy()
start_time = time.time()

for _ in range(1000):
    test_list.pop(0)

time_pop0 = time.time() - start_time
print(f"pop(0) - удаление из начала списка:")
print(f"Время выполнения: {time_pop0:.6f} секунд")
print(f"Длина списка после удалений: {len(test_list)}")
print()

test_list = original_list.copy()
start_time = time.time()

for _ in range(1000):
    test_list.pop()

time_pop = time.time() - start_time
print(f"pop() - удаление с конца списка:")
print(f"Время выполнения: {time_pop:.6f} секунд")
print(f"Длина списка после удалений: {len(test_list)}")
print()

print("=" * 50)
print("СРАВНЕНИЕ:")
print(f"pop(0) быстрее pop() в {time_pop0/time_pop:.2f} раз? НЕТ!")
print(f"pop() быстрее pop(0) в {time_pop0/time_pop:.2f} раз? ДА!")
print()

print("ВЫВОД:")
print("Операция pop() (удаление с конца) значительно быстрее, чем pop(0) (удаление из начала).")
print()
print("ПРИЧИНА (Big O сложность):")
print("1. pop() имеет сложность O(1) - константное время")
print("   - Просто уменьшаем длину списка, не двигая элементы")
print()
print("2. pop(0) имеет сложность O(n) - линейное время")
print("   - Нужно сдвинуть ВСЕ оставшиеся элементы на одну позицию влево")
print("   - Чем больше список, тем медленнее операция")
print("   - При удалении из начала списка из 100k элементов,")
print("     нужно сдвинуть 99,999 элементов!")
print()
print("ЗАКЛЮЧЕНИЕ:")
print("Для частого удаления элементов из начала списка лучше использовать:")
print("- collections.deque (имеет O(1) для операций с обоих концов)")
print("- Или пересмотреть алгоритм, чтобы работать с конца списка")