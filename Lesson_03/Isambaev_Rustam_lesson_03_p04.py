# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def my_pow_simple(x, y):
    x **= y
    return round(x,2)


def my_pow_cycle(x, y):
    x1 = x
    for i in range(-1-y):
        x1 *= x
    return round(1/x1,2)


def my_input(my_type):
    if my_type == 'float':
        while True:
            try:
                my_var = float(input('введите действительное положительное число'))
                if my_var > 0:
                    return my_var
                else:
                    continue
            except ValueError:
                continue
    elif my_type == 'int':
        while True:
            try:
                my_var = int(input('введите целое отрицательное число'))
                if my_var < 0:
                    return my_var
                else:
                    continue
            except ValueError:
                continue

var1 = my_input('float')
var2 = my_input('int')
# простой способ
print(f'{var1} в степени {var2} = {my_pow_simple(var1, var2)}')
# способ с применением цикла
print(f'{var1} в степени {var2} = {my_pow_cycle(var1, var2)}')
