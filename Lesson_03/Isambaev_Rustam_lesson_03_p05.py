# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел
# будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введён после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def check_input(arg1):
    def convert_to_float(subarg1):
        try:
            for i in range(len(subarg1)):
                subarg1[i] = float(subarg1[i])
            return subarg1, False
        except ValueError:
            print('неверный формат - повторите ввод!!!')
            return None, True

    if arg1[-1] == '\\':
        arg1.pop()
        conv_res = convert_to_float(arg1)
        res_list = conv_res[0]
        res_error = conv_res[1]
        res_end = not res_error
    else:
        conv_res = convert_to_float(arg1)
        res_list = conv_res[0]
        res_error = conv_res[1]
        res_end = False
    return res_list, res_error, res_end


sum1 = 0
while True:
    num_string = input('введите через пробел числа, для завершения введите "\\"')
    print(num_string)
    res = check_input(num_string.split(' '))
    if res[1]:
        continue
    else:
        sum1 += sum(res[0])
        print(f'сумма чисел = {sum1}')
    if res[2]:
        break
