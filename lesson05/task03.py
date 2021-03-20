employee_dict = {}
low_salary = []
with open("file03.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        key, value = line.split()
        employee_dict[key] = float(value)
for item in employee_dict.items():
    if item[1] < 20000:
        low_salary.append(item[0])
print(f"Сотрудники с окладом менее 20 тыс.: {', '.join(low_salary)}")
print(f"Средний оклад сотрудников: {sum(employee_dict.values()) / len(employee_dict)}")
