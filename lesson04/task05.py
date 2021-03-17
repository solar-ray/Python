from functools import reduce


def my_func(el1, el2):
    return el1 * el2


print(f"Список: {[j for j in range(99, 1001) if j % 2 == 0]}")
print(f"Произведение всех элементов списка: {reduce(my_func, [i for i in range(99, 1001) if i % 2 == 0])}")
