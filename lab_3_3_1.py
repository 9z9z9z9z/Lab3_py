import datetime
from time import strftime
import date_tools
import date_calculator


def nearest_date(*params):  # дд.мм.гггг
    today = datetime.datetime.today()
    dates = [datetime.datetime.strptime(param, "%d.%m.%Y") for param in params]
    dates.append(today)
    dates.sort()
    index = dates.index(today)
    try:
          if

    print("end")


nearest_date("11.11.2001", "11.11.1990", "11.11.2003", "11.11.2002")
