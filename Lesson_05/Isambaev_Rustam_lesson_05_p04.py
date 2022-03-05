# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import os

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
translate = []
with open('./mydata1/onetwothreefour.txt', 'r', encoding='ascii') as my_file:
    while True:
        my_str = my_file.readline()
        if not my_str:
            break
        my_str = my_str.split()
        my_str[0] = my_dict[my_str[0]]
        translate += [' '.join(my_str)]
print(translate)
if not os.path.exists('./mydata'):
    os.mkdir('./mydata')
with open('./mydata/translate.txt', 'w', encoding='utf-8') as my_translate:
    for line in translate:
        print(line, end='' if translate.index(line) + 1 == len(translate) else '\n', file=my_translate)
