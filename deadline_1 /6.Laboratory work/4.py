text = input("Введите произвольный текст: ").strip()
range_input = input("Введите диапазон: ").strip()

try:
    start_str, end_str = range_input.split()
    start = int(start_str)
    end = int(end_str)

    substring = text[start-1:end]
    
    print(f"Подстрока с {start} по {end} символ:")
    print(substring)
except ValueError:
    print("Ошибка: введите два числа через пробел")
except IndexError:
    print("Ошибка: указанный диапазон выходит за пределы строки")