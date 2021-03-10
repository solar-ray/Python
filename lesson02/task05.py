rating = [7, 5, 3, 3, 2]

print(rating)
while True:
    user_num = input("Введите число или 'q' для выхода: ")
    if user_num != 'q':
        rating.append(int(user_num))
        rating.sort(reverse=True)
        print(rating)
    else:
        break
