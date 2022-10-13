import datetime
from time import strftime

import date_tools
import date_calculator


def nearest_date(*params):    # дд.мм.гггг
      dates = [datetime.datetime.strptime(param, "%d.%m.%Y") for param in params]
      dates.sort()
      sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]

      print(dates)
      print(dates[1] - dates[0])
      print(sorteddates)



      print("end")



nearest_date("11.11.2001", "11.11.1990", "11.11.2003", "11.11.2002")