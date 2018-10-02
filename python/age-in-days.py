from datetime import date

def age_in_days(year, month, day):
    """Computes age in days from input"""
    birth_date = date(year, month, day)
    today = date.today()
    difference = today - birth_date 
    return difference.days

year = int(input("What year? "))
month = int(input("What month? "))
day = int(input("What day? "))
print( age_in_days(year, month, day) )
