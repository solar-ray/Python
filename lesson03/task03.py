def my_func(num1, num2, num3):
    numbers_list = [num1, num2, num3]
    numbers_list.remove(min(numbers_list))
    return sum(numbers_list)


print(my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
              int(input("Введите третье число:"))))
