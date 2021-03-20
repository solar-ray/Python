import json
firm_profit = {}
avg_profit_dict = {}
summary_list = []
sum_profit = 0
avg_profit = None
work_with_profit = 0
with open('file07.txt', 'r') as my_file:
    for line in my_file:
        name, ownership, earnings, expenses = line.split()
        firm_profit[name] = float(earnings) - float(expenses)
        if firm_profit.get(name) >= 0:
            sum_profit += firm_profit.get(name)
            work_with_profit += 1
    if work_with_profit > 0:
        avg_profit = sum_profit / work_with_profit
    else:
        print(f"Компании работают без прибыли!")
    avg_profit_dict = {"average_profit": avg_profit}
    summary_list.append(firm_profit)
    summary_list.append(avg_profit_dict)
with open('file07.json', 'w', encoding="utf-8") as my_json:
    json.dump(summary_list, my_json)
    print(f"Создан json: {json.dumps(summary_list)}")
