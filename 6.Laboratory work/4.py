text = input("Введите произвольный текст: ")

segment = input("Введите диапазон символов (начало конец): ")

numbers = segment.split()

if len(numbers) == 2:
    start, end = map(int, numbers)
    
    start_index = start - 1
    end_index = end
    
    if 0 <= start_index < len(text) and end_index <= len(text) and start_index <= end_index:
        substring = text[start_index:end_index]
        print("\nПодстрока по заданному диапазону:")
        print(substring)
    else:
        print("Ошибка: указанный диапазон выходит за пределы текста!")
else:
    print("Ошибка: нужно ввести два числа через пробел!")