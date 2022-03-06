# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
import Isambaev_Rustam_my_module as My_module

my_digit = My_module.my_integer_number_input('введите положительное целое число n', 'число должно быть '
                                                                                    'положительным!!!')
my_sum = my_digit + int(f'{my_digit}{my_digit}') + int(f'{my_digit}{my_digit}{my_digit}')
print('сумма чисел n + nn + nnn = ', my_sum)
