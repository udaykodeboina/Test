import datetime

now = datetime.datetime.now()
start_month = datetime.datetime(now.year, now.month, 1)
date_on_next_month = start_month + datetime.timedelta(35)
start_next_month = datetime.datetime(date_on_next_month.year, date_on_next_month.month, 1)
last_day_month = start_next_month - datetime.timedelta(1)