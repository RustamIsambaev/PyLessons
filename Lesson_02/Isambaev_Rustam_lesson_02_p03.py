# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.
import Isambaev_Rustam_my_module as My_module


def input_month(msg):
    my_var = My_module.my_integer_number_input(msg, 'номер месяца должно быть положительное число')
    if my_var not in range(1, 13):
        print('введенное число не соответствует диапазону от 1 до 12')
        return input_month(msg)
    else:
        return my_var


My_month = input_month('введите номер месяца в диапазоне целых чисел от 1 до 12')
# Решение через list
My_seasons_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
print(f'месяц {My_month} относится к времени года {My_seasons_list[My_month - 1]}')
# Решение через dict
My_seasons_dict = {(1, 2, 12): 'Зима', (3, 4, 5): 'Весна', (6, 7, 8): 'Лето', (9, 10, 11): 'Осень'}
print(f'месяц {My_month} относится к времени года {[y for i, y in My_seasons_dict.items() if My_month in i][0]}')
