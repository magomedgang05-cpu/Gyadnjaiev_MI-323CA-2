fruits = {
    'яблоки': 5,
    'бананы': 3,
    'апельсины': 10,
    'арбузы': 33
}

print("Начальное количество фруктов:")
for fruit, quantity in fruits.items():
    print(f"За прилавком есть {quantity} {fruit}")

print("\n" + "="*40)

fruits['яблоки'] -= 2
print("Продали 2 яблока")

fruits['арбузы'] = 0
print("Ашот Похититель Арбузов украл все арбузы!")

print("\n" + "="*40)

print("Итоговое количество фруктов:")
for fruit, quantity in fruits.items():
    print(f"За прилавком осталось {quantity} {fruit}")