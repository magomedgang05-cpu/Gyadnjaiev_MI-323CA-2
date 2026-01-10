import random
temperatures = [random.randint(10, 25) for _ in range(14)]
print(f"Температуры (°C): {temperatures}")

max_temp = max(temperatures)
min_temp = min(temperatures)

average_temp = sum(temperatures) / len(temperatures)

days_above_avg = len([temp for temp in temperatures if temp > average_temp])

sorted_temps = sorted(temperatures)

temperatures_f = [temp * 9/5 + 32 for temp in temperatures]

print("АНАЛИЗ ТЕМПЕРАТУР:")
print(f"• Максимальная температура: {max_temp}°C")
print(f"• Минимальная температура: {min_temp}°C")
print(f"• Средняя температура: {average_temp:.1f}°C")
print(f"• Количество дней с температурой выше средней: {days_above_avg}")
print(f"• Отсортированные температуры: {sorted_temps}")

print("ПРЕОБРАЗОВАНИЕ В ФАРЕНГЕЙТЫ:")
print(f"Температуры в °F: {[round(f, 1) for f in temperatures_f]}")

print(" ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА:")
print(f"• Диапазон температур: {max_temp - min_temp}°C")
print(f"• Дней с температурой ниже средней: {len(temperatures) - days_above_avg}")

print("ГРАФИЧЕСКОЕ ПРЕДСТАВЛЕНИЕ:")
for temp in range(min_temp, max_temp + 1):
    count = temperatures.count(temp)
    if count > 0:
        bar = "|" * count
        print(f"{temp:2}°C: {bar} ({count} дней)")