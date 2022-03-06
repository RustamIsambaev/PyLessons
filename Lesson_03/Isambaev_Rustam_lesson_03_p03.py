# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.sort()
    return sum(my_list[1:])


def my_input(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print('введи число')
            continue


var1 = my_input('1й аргумент ')
var2 = my_input('2й аргумент ')
var3 = my_input('3й аргумент ')
print(my_func(var1, var2, var3))
