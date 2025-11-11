text = input("Введите произвольный текст: ")

step = int(input("Введите шаг: "))

result = text[::step]

print("\n Текст с шагом", step, ":")
print(result)