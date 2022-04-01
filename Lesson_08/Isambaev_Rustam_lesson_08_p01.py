class Myexception(Exception):
    def __init__(self, msg):
        self.msg = msg


class Mydate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def datevalid(day, month, year):
        def daysinmonth(monthn, yeartype):
            daysinmonthdict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            if monthn == 2 and not yeartype:
                return 29
            else:
                return daysinmonthdict[monthn]

        if month in range(1, 13) and year > 1582 and day in range(1, daysinmonth(month, year % 4)):
            return True
        else:
            return False

    @classmethod
    def datediv(cls, datestr):
        day = int(datestr[:2])
        month = int(datestr[3:5])
        year = int(datestr[6:])
        if cls.datevalid(day, month, year):
            return cls(day, month, year)
        else:
            raise Myexception('неверные данные!')


try:
    date1 = Mydate.datediv('01.12.2000')
    print(f'{date1.day}-{date1.month}-{date1.year}')
    date1 = Mydate.datediv('00.12.2000')
except Myexception as err:
    print(err)
