from sys import argv

try:
    file, user_time, user_rate, user_bonus = argv
except ValueError:
    print("Недостаточно параметров")
    exit()


def calc_salary(time, rate, bonus):
    try:
        time = float(time)
        rate = float(rate)
        bonus = float(bonus)
        res = time * rate + bonus
        print(f'Заработная плата сотрудника  {res}')
    except ValueError:
        print('Не число')


calc_salary(user_time, user_rate, user_bonus)
