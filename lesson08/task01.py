class Date:
    def __init__(self, user_date):
        self.user_date = str(user_date)

    @classmethod
    def extract(cls, user_date):
        my_date = []
        for i in user_date.split('-'):
            my_date.append(int(i))
        return f"{my_date[0]}-{my_date[1]}-{my_date[2]}"

    @staticmethod
    def validate(day: int, month: int, year: int):
        if year > 0 and (month in (1, 3, 5, 7, 8, 10, 12) and 1 <= day <= 31) or (
                month in (4, 6, 9, 11) and 1 <= day <= 30) \
                or (month == 2 and 1 <= day <= 28):
            return "Дата валидна"
        else:
            return "Дата не валидна"

    def __str__(self):
        return f"Текущая дата {Date.extract(self.user_date)}"


today = Date('31-3-2021')
print(today)
print(Date.validate(1, 3, 2022))
print(today.validate(32, 17, 2021))
