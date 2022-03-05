# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
import Isambaev_Rustam_my_module as My_module
my_digit = My_module.my_integer_number_input('введите положительное целое число', 'число должно быть '
                                                                                  'положительным!!!')
max_digit = 0
while my_digit:
    if max_digit < my_digit % 10:
        max_digit = my_digit % 10
    my_digit //= 10
else:
    print(max_digit, '- самая большая цифра в введенном числе')
