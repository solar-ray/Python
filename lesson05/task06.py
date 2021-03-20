import re

schedule = {}

with open('file06.txt', 'r', encoding="utf-8") as my_file:
    for line in my_file:
        subject, *lessons = line.split()
        schedule[subject] = lessons
print(f"Исходные данные: {schedule}")
for i in schedule.keys():
    s = ''.join(schedule.get(i))
    s = re.findall(r'\d+', s)
    schedule[i] = sum(map(int, s))
print(f"Итог: {schedule}")
