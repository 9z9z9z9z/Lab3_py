import datetime


def nearest_date(*params):  # дд.мм.гггг
    today = datetime.datetime.today()
    dates = [datetime.datetime.strptime(param, "%d.%m.%Y") for param in params]
    dates.append(today)
    dates.sort()
    index = dates.index(today)

    if len(dates) == 1:
        return None

    elif index == 0:
        return dates[index + 1]

    elif index == len(dates) - 1:
        return dates[index - 1]

    elif abs(dates[index] - dates[index - 1]) < abs(dates[index] - dates[index + 1]):
        return dates[index - 1]

    else:
        return dates[index + 1]


print(str(nearest_date("01.01.2050", "12.04.2011", "31.12.1970").date()))
