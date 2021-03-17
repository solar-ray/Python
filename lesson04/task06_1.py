from itertools import count


for i in count(int(input("Введите целое число: "))):
    print(i)
    if i == 10:
        exit()
