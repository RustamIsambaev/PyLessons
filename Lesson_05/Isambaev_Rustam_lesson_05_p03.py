# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
staff_schedule = []
with open('./mydata1/сотрудники.txt', 'r', encoding='windows-1251') as my_file:
    while True:
        my_str = my_file.readline()
        if not my_str:
            break
        my_str = my_str.split()
        b = float(my_str[1])
        my_str += [float(my_str[1])]
        my_str = my_str[0:1] + [my_str[2]]
        staff_schedule += [my_str]
print('список сотрудников заработная плата которых ниже 20 000.00р.')
b = 0
for i in staff_schedule:
    if i[1] < 20000:
        print(i[0])
    b += i[1]
print(f'средняя величина дохода сотрудников составляет {round(b/len(staff_schedule),2)}р')
