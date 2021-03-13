def user_info(firstname, lastname, year, city, email, phone):
    return f"{firstname} {lastname} {year} {city} {email} {phone}"


print("Введите данные пользователя.")
print(user_info(firstname=input("Имя: "), lastname=input("Фамилия: "), year=input("Год рождения: "),
                city=input("Город: "), email=input("e-mail: "), phone=input("Номер телефона: ")))
