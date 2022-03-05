# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
import os

if not os.path.exists('./mydata'):
    os.mkdir('./mydata')

with open('./mydata/data.txt', 'w', encoding='utf-8') as my_file:
    line = ''
    while True:
        line = input(">:")
        if line == '':
            break
        print(line, file=my_file)
