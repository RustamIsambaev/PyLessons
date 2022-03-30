class MyCheck(Exception):
    pass


mylist = list()
while True:
    a = input('введите число (для завершения введите ''stop'')')
    if a == 'stop':
        break
    else:
        try:
            if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
                mylist.append(int(a))
            elif a.count('.') == 1:
                if a.replace('.', '').isdigit() or (a[0] == '-' and a[1:].replace('.', '').isdigit()):
                    mylist.append(float(a))
            else:
                raise MyCheck
        except MyCheck:
            print('введите число!')
print(mylist)
print(sum(mylist))
