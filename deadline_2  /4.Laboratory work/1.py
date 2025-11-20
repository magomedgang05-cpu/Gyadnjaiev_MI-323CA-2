grades = []

grades.append(1)
grades.append(2)
grades.append(5)
grades.append(5)
grades.append(4)

print("Текущие оценки:", grades)

del grades[0]
grades.pop()

average_grade = sum(grades) / len(grades)
print("Средний балл:", average_grade)

print("Итоговые оценки:", grades)