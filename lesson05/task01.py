with open("file01.txt", "w") as my_file:
    while True:
        user_input = input("Введите строку: ")
        if not user_input:
            break
        print(user_input, file=my_file)
