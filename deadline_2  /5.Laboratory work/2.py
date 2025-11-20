students = [
    ("Магомед", 18, 5.0),
    ("Степан Б", 18, 4.8),
    ("Анатолий С-С-Слабадсков", 22, 4.5),
    ("Амир Крипс", 21, 4.5),
    ("Анастасия", 21, 2.5)
]

print("Студенты старше 20 лет:")
for name, age, avg_grade in students:
    if age > 20:
        print(f"- {name} ({age}), средний балл: {avg_grade}")

print()

best_student = max(students, key=lambda student: student[2])
print(f"Лучший студент: {best_student[0]}, средний балл: {best_student[2]}")

print()

sorted_students = sorted(students, key=lambda student: student[0])
print("Отсортированный список студентов по имени:")
for name, age, avg_grade in sorted_students:
    print(f"- {name} ({age}), средний балл: {avg_grade}")