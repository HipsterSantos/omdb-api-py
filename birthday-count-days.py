from datetime import datetime
from time import time
def print_header():
    print("____________________________")
    print("\t\tBirthday Count Days")
    print("____________________________")
def get_birthdays(**kwargs):
    print("Tell us when you were born")
    year = input("[yyyy] year = ")
    day = input("[DD] Day =")
    month = input("[MM] Month = ")
    birthday = datetime(int(year), int(month), int(day))
    return birthday
def compute_days(or_date,now):
    now = now
    date2 = datetime(or_date.year, or_date.month, or_date.day)
    dt: object = now - date2
    days = dt.total_seconds()  / 60 /60 / 24
    return days

def print_birthdays(birthdays):
    pass

def main():
    print_header()
    birthdays = get_birthdays()
    print(birthdays)
    now = datetime.now()
    numDays = compute_days(birthdays,now)
    print(numDays)
main()