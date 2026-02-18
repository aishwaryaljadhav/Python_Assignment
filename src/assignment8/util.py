import calendar

def finding_day(month, day, year):
    try:
        weekday = calendar.weekday(year, month, day)
        return calendar.day_name[weekday].upper()
    except:
        return None
