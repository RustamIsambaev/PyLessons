# мой модуль
def my_integer_number_input(my_question, not_positive_wrong_message, zero=False):
    while True:
        try:
            my_var = int(input(my_question))
            if my_var <= 0 and not_positive_wrong_message:
                if my_var == 0 and zero:
                    return my_var
                print(not_positive_wrong_message)
                continue
            return my_var
        except ValueError:
            print('введите целое число!!!')
            continue


def my_float_number_input(my_question, not_positive_wrong_message, zero=False):
    while True:
        try:
            my_var = float(input(my_question).replace(',', '.'))
            if my_var <= 0 and not_positive_wrong_message:
                if my_var == 0 and zero:
                    return my_var
                print(not_positive_wrong_message)
                continue
            return my_var
        except ValueError:
            print('Введите число *.* или *,*')
            continue
