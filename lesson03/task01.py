def my_division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return None


num1 = int(input("Введите делимое: "))
num2 = int(input("Введите делитель: "))
print(my_division(num1, num2))
