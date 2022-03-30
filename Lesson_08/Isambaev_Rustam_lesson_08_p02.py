class MyCheck(Exception):
    pass


try:
    a = int(input('введите знаменатель'))
    if a == 0:
        raise MyCheck
    print(100 / a)
except MyCheck:
    print('знаменатель не равен нулю!')
