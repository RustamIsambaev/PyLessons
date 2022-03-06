# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
import os
import functools

if not os.path.exists('./mydata'):
    os.mkdir('./mydata')

# создаем (программно) текстовый файл
with open('./mydata/data1.txt', 'w') as my_file:
    while True:
        number = input('введите целое число (для прекращения ввода: Enter)')
        if number:
            try:
                int(number)
                print(f'{number} ', end='', file=my_file)
            except ValueError:
                print('неверный формат данных!!!')
            finally:
                continue
        break
# считаем сумму чисел в файле
with open('./mydata/data1.txt', 'r') as my_file:
    my_str = my_file.read()[:-1]
    ml = [int(i) for i in my_str.split(' ')]
print(f'сумма чисел = {functools.reduce(lambda x, y: x + y, ml)}')
