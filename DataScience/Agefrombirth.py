import datetime as dt

day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))
d1= dt.datetime.now()
d2=int(d1.year)
#d3=int(d1.month)
#d4=int(d1.day)
Current_Age_year=d2-year
#Current_Age_month=d3-month
#Current_Age_day=d4-day
print(f"Your Current Age is: {Current_Age_year} Years")
