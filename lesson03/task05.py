def sum_sequence():
    final_sum = 0
    exit_char = False
    while not exit_char:
        user_input = input("Введите числа через проблел, для выхода введите 'q': ").split()
        res = 0
        for i in range(len(user_input)):
            if user_input[i].lower() == 'q':
                exit_char = True
            else:
                res += float(user_input[i])
        final_sum += res
        print(f'Сумма последних введенных чисел: {res}')
    print(f'Итоговая сумма: {final_sum}')


sum_sequence()
