user_string = input("Введите несколько слов, разделяя их пробелом:").split()

counter = 0
for i in user_string:
    counter += 1
    print(f"{counter}. {i[0:10]}")
