earnings = float(input("Введите сумму выручки:"))
costs = float(input("Введите сумму издержек:"))
if earnings > costs:
    income = earnings - costs
    print(f"Фирма работает с прибылью. Прибыль: {income}")
    profitability = round(earnings / costs, 4) * 100
    print(f"Рентабельность: {profitability}%")
    employee_qty = int(input("Введите численность сотрудников:"))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {round(income / employee_qty, 2)}")
elif costs > earnings:
    print("Фирма работает в убыток.")
else:
    print("Фирма работает с нулевой прибылью.")
