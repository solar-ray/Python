class MyDivideByZero(Exception):
    def __init__(self, msg):
        self.msg = msg


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))
try:
    if b == 0:
        raise MyDivideByZero("Деление на ноль!")
    print(a / b)
except MyDivideByZero as e:
    print(e)
