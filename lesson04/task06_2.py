from itertools import cycle

my_list = [300, 2, 12, 44, 1]
repeat_counter = 0
repeat_counter = 0

print(len(my_list))
for i in cycle(my_list):
    print(i)
    repeat_counter += 1
    if repeat_counter == len(my_list) * 10:
        exit()
