some_list = input("Введите несколько чисел, разделяя их пробелом:").split()
print(some_list)
c = 0
for i in range(int(len(some_list) / 2)):
    some_list[c], some_list[c + 1] = some_list[c + 1], some_list[c]
    c += 2
print(some_list)
