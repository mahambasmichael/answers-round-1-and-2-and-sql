from datetime import datetime,timedelta
import calendar 

def compute_prev_date(dates):
    prev_dates = []
    for date in dates:
        date_obj= datetime.strptime(date,'%Y-%m-%d')
        prev_date = date_obj-timedelta(date=1)
        month_abbr=calendar.month_abbr[prev_date.month]
        prev_dates.append(f"{prev_date.day} {month_abbr}{prev_date.year}")
        return prev_dates