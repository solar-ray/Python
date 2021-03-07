a = int(input("Введите результат первого дня тренировок:"))
b = int(input("Введите желаемый результат тренировки:"))
print(f"1-й день: {a}")
day_count = 2
while a < b:
    a = a * 1.1
    print(f"{day_count}-й день: {round(a, 2)}")
    if a >= b:
        print(f"Ответ: на {day_count}-й день спортсмен достиг результата — не менее {b} км.")
    day_count = day_count + 1
