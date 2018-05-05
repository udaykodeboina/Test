import datetime
 
def get_last_day_of_the_month(y, m):
    '''
    Returns an integer representing the last day of the month, given
    a year and a month.
    '''
 
    # Algorithm: Take the first day of the next month, then count back
    # ward one day, that will be the last day of a given month. The 
    # advantage of this algorithm is we don't have to determine the 
    # leap year.
 
    m += 1
    if m == 13:
        m = 1
        y += 1
 
    first_of_next_month = datetime.date(y, m, 1)
    last_of_this_month = first_of_next_month + datetime.timedelta(-1)
    return last_of_this_month.day