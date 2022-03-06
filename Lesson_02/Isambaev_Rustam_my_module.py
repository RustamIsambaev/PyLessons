# мой модуль
def my_integer_number_input(my_question, not_positive_wrong_message, zero=False, enter=False):
    while True:
        try:
            my_var = input(my_question)
            my_var = int(my_var)
            if my_var <= 0 and not_positive_wrong_message:
                if my_var == 0 and zero:
                    return my_var
                print(not_positive_wrong_message)
                continue
            return my_var
        except ValueError:
            if enter and my_var == '':
                return my_var
            else:
                print('введите целое число!!!')
            continue


def my_float_number_input(my_question, not_positive_wrong_message, zero=False, enter=False):
    while True:
        try:
            my_var = input(my_question)
            my_var = float(my_var.replace(',', '.'))
            if my_var <= 0 and not_positive_wrong_message:
                if my_var == 0 and zero:
                    return my_var
                print(not_positive_wrong_message)
                continue
            return my_var
        except ValueError:
            if enter and my_var == '':
                return my_var
            else:
                print('Введите число *.* или *,*')
            continue
