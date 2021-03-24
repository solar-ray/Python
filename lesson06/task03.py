class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.firstname: str = name
        self.lastname: str = surname
        self.position: str = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.firstname + ' ' + self.lastname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


employee = Position(input("Введите имя: "), input("Введите фамилию: "), input("Укажите должность: "),
                    input("Укажите оклад: "), input("Укажите премию: "))
print(employee.get_full_name())
print(employee.position)
print(employee.get_total_income())
