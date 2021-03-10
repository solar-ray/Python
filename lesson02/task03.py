seasons = ["Зима", "Весна", "Лето", "Осень"]
seasons_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
                10: "Осень", 11: "Осень", 12: "Зима"}
month_num = int(input("Введите номер месяца:"))

print("Через список:")
if month_num == 12 or 1 <= month_num <= 2:
    print(seasons[0])
elif 2 < month_num <= 5:
    print(seasons[1])
elif 5 < month_num <= 8:
    print(seasons[2])
elif 8 < month_num < 12:
    print(seasons[3])
else:
    print("Месяца с таким номером не существует.")

print("Через словарь:")
if month_num < 1 or month_num > 12:
    print("Месяца с таким номером не существует.")
else:
    print(seasons_dict.get(month_num))
