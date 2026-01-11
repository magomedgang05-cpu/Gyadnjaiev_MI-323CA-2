students = [
    ("Магомед", 20, 5.0),
    ("Заур", 21, 3.1),
    ("Настя", 19, 4.1),
    ("Степан", 20, 3.9),
    ("Амир", 23, 4.5)
]

print("Студенты старше 20 лет:")
for name, age, score in students:
    if age > 20:
        print(f"– {name} ({age}), средний балл: {score}")

max_score_student = max(students, key=lambda x: x[2])
print(f"\nЛучший студент:")
print(f"– {max_score_student[0]} ({max_score_student[1]}), средний балл: {max_score_student[2]}")

sorted_students = sorted(students, key=lambda x: x[0])
print("\nПолный отсортированый список студентов:")
for name, age, score in sorted_students:
    print(f"– {name} ({age}), средний балл: {score}")