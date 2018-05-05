from datetime import datetime
def last_date_of_month(year,month):
    last_days=[31,30,29,28]
    for i in last_days:
        try:
            end=datetime(year,month,i)
        except ValueError:
            continue
        else:
            return end.date()
    return None
        