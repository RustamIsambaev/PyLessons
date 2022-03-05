# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
import Isambaev_Rustam_my_module as My_module

my_time = My_module.my_integer_number_input('введите время в секундах', 'значение времени должно быть целым '
                                                                        'положительным числом!!!')
my_hour = my_time // (60 * 60)
if my_hour > 23:
    my_hour %= 24
my_minute = my_time % (60 * 60) // 60
my_second = my_time % (60 * 60) % 60
print(f'{my_hour:02}:{my_minute:02}:{my_second:02}')
