import datetime


def nearest_date(*params):    # дд.мм.гггг
      today = datetime.date.today()
      today_int = today.day + today.month * 30 + today.year * 365
      base = [0] * len(params)  # Массив дат
      clone = list()  # Массив разностей дат

      for k in range(len(params)):
            tmp = params[k].split(".")
            base[k] += int(tmp[0]) + int(tmp[1]) * 30 + int(tmp[2]) * 365
            clone.append(base[k] - today_int)
            print(clone[k])

      base = (sorted(base, key=lambda num: clone))

      print("end")


nearest_date("11.11.2031", "11.11.1990")