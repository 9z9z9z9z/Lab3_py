import datetime


def nearest_date(*params):    # дд.мм.гггг
      today = datetime.date.today()
      for data in params:
            base = list()     # Массив дат
            clone = list()    # Массив разностей дат
            tmp = data.split(".")
            for i in range(3):
                  base.append(int(tmp[i]))
                  clone.append(abs(today.day - int(tmp[i])) + abs(today.month - int(tmp[i])) * 30 + abs(today.year - int(tmp[i])) * 365)


            print("end")


nearest_date("11.11.2001")