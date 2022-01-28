"""
Program that gives the day of the week for any given date
Agustina Varas
01/23/2022

"""
from datetime import date



#Adds up number of days from the year given by user
#leap years are every four years except if they are divisble by 100 they must 
#also be divisible by 400 to be a leap year
def year_days(year):
    total_days = 0
    while year > 1:
        if year % 100 == 0:
            if year % 400 == 0:
                total_days += 1
        elif year % 4 == 0:
            total_days += 1
        total_days += 365
        year -= 1
    return total_days
        

# add up the number of days in that year up to the month that is given
# example: if the given month is februrary the function returns 31
def month_days (month):
    days_from_month = 0
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    while (i < month - 1):
        days_from_month += days_in_month[i]
        i += 1
    return days_from_month


# adds up the total days at the given date
def total_days(day, month, year):
    total_days = day
    total_days += year_days(year)
    total_days += month_days(month)
    return total_days


#returns a string corresponding to the day of the week
def day_of_week(day, month, year):
    days_of_week = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    total = total_days(day, month, year)
    day_of_week = total % 7
    return days_of_week[day_of_week]


def days_difference(day, month, year):
    today = date.today()
    today_total = total_days(today.day, today.month, today.year)
    other_date_total = total_days(day, month, year)
    return today_total - other_date_total
    

def calculate_date():
    print("Enter the date in mm/dd/yyyy format: ")
    date = input()
    date_seperated = date.split("/")
    day = int(date_seperated[1])
    month = int(date_seperated[0])
    year = int(date_seperated[2])
    print(date + " is a " + day_of_week(day, month, year) + ". ")
    difference = days_difference(day, month, year)
    if difference < 0:
        
        print(str(abs(difference)) + " days until " + date)
    elif difference > 0:
        print(date + " was " + str(difference) + " days ago." )
    else:
        print(date + " is today!")
    
calculate_date()

