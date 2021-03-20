with open("file02.txt", "r") as my_file:
    lines = my_file.readlines()
    print(f"Количество строк в файле: {len(lines)}")
    line_number = 0
    for line in lines:
        words_list = str(line).split()
        print(f"Строка {line_number + 1}: {len(words_list)} слов")
        line_number += 1
