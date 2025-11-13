# Задание 1: Сумма чисел от 1 до n
n = int(input("Введите число n: "))

total = 0
numbers = []  # Список для хранения чисел

for i in range(1, n + 1):
    total += i
    numbers.append(i)

# Формируем вывод как в примере
explanation = " + ".join(map(str, numbers))
print(f"{total} ({explanation})")