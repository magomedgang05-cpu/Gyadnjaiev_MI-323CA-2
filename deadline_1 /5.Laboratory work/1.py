num1 = float(input("Введите первое число:"))

num2 = float(input("Введите второе число:"))
print("Результат вычислений")
print(f"сложение: {num1} + {num2} = {num1 + num2}")
print(f"вычитание: {num1} - {num2} = {num1 - num2}")
print(f"умножение: {num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"деление: {num1} / {num2} = {num1 / num2}")
else:
    print("Деление: на ноль делить нельзя!")