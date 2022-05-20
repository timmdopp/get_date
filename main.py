from datetime import timedelta, date, datetime as dt


def title():
    title_date = f'{your_date} to {todate}'
    return title_date

def both_dates():
    return your_date, todate

daysBack = int(input("How many days ago?") or "30")
time_fr = int(input("How many days to check?") or daysBack+1)
your_date = (dt.now() - timedelta(daysBack)).strftime("%m/%d/%Y")
todate = (dt.now() - timedelta(daysBack)+ timedelta(time_fr)).strftime("%m/%d/%Y")

print(both_dates())
