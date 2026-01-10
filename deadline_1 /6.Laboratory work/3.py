text = input("Введите произвольный текст: ").strip()

try:
    step = int(input("Введите шаг: ").strip())
    result = text[::step]
    print("Текст с заданным шагом:")
    print(result)
except ValueError:
    print("Ошибка: шаг должен быть целым числом")
except Exception as e:
    print(f"Произошла ошибка: {e}")