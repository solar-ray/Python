translation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
translated_file = []
with open('file04.txt', 'r', encoding="utf-8") as my_file:
    for line in my_file:
        line = line.split(" — ")
        translated_file.append(translation[line[0]] + " — " + line[1])
with open('file04_translated.txt', 'w', encoding="utf-8") as my_file:
    my_file.writelines(translated_file)
