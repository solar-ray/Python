user_time = int(input("Введите время в секундах:"))
minutes, seconds = divmod(user_time, 60)
hours, minutes = divmod(minutes, 60)
print(f"{hours}:{minutes}:{seconds}")
