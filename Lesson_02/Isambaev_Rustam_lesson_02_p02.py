# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов
# нужно использовать функцию input().
My_list = []
while True:
    new_element = input('введите значение элемента или введите Enter для завершения:')
    if new_element:
        My_list += new_element
    else:
        break
print(My_list)
for i in range(len(My_list)):
    if not i % 2:
        if i + 1 < len(My_list):
            My_list[i], My_list[i + 1] = My_list[i + 1], My_list[i]
        else:
            pass
print(My_list)
