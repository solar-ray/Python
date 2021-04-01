class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg


numbers_list = []
user_input = None
while user_input.lower() != "stop":
    user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")
    if user_input == "stop":
        break
    try:
        if not user_input.isdigit():
            raise MyError(f"'{user_input}' - не число.")
        numbers_list.append(int(user_input))
    except MyError as e:
        print(e)
print(f"Создан список чисел: {numbers_list}")
