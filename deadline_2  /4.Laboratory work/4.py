temperatures = [14, 11, 18, 1, 30, 32, 29, 40, 13, 21, 15, 19, 33, 11,]

max_temp = max(temperatures)
min_temp = min(temperatures)

average_temp = sum(temperatures) / len(temperatures)

days_above_average = 0
for temp in temperatures:
    if temp > average_temp:
        days_above_average += 1

sorted_temperatures = sorted(temperatures)

temperatures_fahrenheit = []
for temp in temperatures:
    fahrenheit = temp * 9/5 + 32
    temperatures_fahrenheit.append(round(fahrenheit, 1))

print("Температуры:", temperatures)
print(f"Максимальная: {max_temp}°C")
print(f"Минимальная: {min_temp}°C")
print(f"Средняя: {average_temp:.1f}°C")
print(f"Дней выше средней: {days_above_average}")
print(f"Отсортированные температуры: {sorted_temperatures}")
print(f"Температуры в Фаренгейтах: {temperatures_fahrenheit}")