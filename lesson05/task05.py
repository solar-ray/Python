with open('file05.txt', 'w', encoding="utf-8") as my_file:
    my_file.write(input("Введите числа через пробел: "))
with open('file05.txt', 'r', encoding="utf-8") as my_file:
    line_list = list(my_file.readlines())
line_str = line_list[0].split()
print(line_str)
print(sum(map(int, line_str)))
