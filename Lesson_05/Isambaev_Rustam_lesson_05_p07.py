# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
# о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчёт средней прибыли её не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import functools
import os
import json

if not os.path.exists('./mydata'):
    os.mkdir('./mydata')

my_data = [{}, {}]
with open('./mydata1/фирмы.txt', 'r', encoding='windows-1251') as my_file:
    while True:
        line = my_file.readline()
        if line:
            firm_data = line.split()
            profit = int(firm_data[2]) - int(firm_data[3])
            my_data[0][firm_data[0]] = profit
        else:
            break
my_data[1]['average profit'] = round(functools.reduce(lambda x, y: x + y,
                                                      [profit for profit in my_data[0].values() if profit > 0]) / len(
    my_data[0]))
with open('./mydata/firms.json', 'w') as my_file:
    json.dump(my_data, my_file)
