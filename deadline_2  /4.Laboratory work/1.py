grades = []

import random
for _ in range(5):
    grades.append(random.randint(1, 5))

print(f"Текущие оценки: {grades}")

if len(grades) >= 2:
    first_removed = grades.pop(0)
    last_removed = grades.pop()
    print(f"Удалена первая оценка: {first_removed}")
    print(f"Удалена последняя оценка: {last_removed}")
elif len(grades) == 1:
    removed = grades.pop()
    print(f"Удалена единственная оценка: {removed}")
else:
    print("Список оценок пуст!")

if grades:
    average_grade = sum(grades) / len(grades)
    print(f"Средний балл: {average_grade:.1f}")
else:
    print("Средний балл: нет оценок для расчета")

print(f"Итоговые оценки: {grades}")