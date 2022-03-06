# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У
# пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
import Isambaev_Rustam_my_module as My_module


def find_last_position(list_arg, element, start_index):
    if element in list_arg[start_index + 1:]:
        return find_last_position(list_arg, element, list_arg.index(element, start_index + 1))
    else:
        return start_index + 1


my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
    my_rating = My_module.my_integer_number_input('введите рейтинг (натуральное число) или Enter для завершения: ',
                                                  'число должно быть натуральным!!!', enter=True)
    if my_rating:
        if my_rating in my_list:
            my_list.insert(find_last_position(my_list, my_rating, my_list.index(my_rating)), my_rating)
        else:
            if my_rating > my_list[0]:
                my_list.insert(0, my_rating)
            else:
                for i, v in enumerate(my_list,1):
                    if i < len(my_list):
                        if v > my_rating > my_list[i]:
                            my_list.insert(i, my_rating)
                            break
                    else:
                        my_list.insert(i, my_rating)
                        break
        print(my_list)
    else:
        break
