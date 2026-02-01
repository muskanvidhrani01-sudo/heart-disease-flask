import datetime as dt

d1= dt.datetime.now()
d2=d1.year
Current_Age=int(input("Enter your current Age: "))
#Current_Year=2025
Golden_left=100-Current_Age
Golden_Age=d2+Golden_left
print(f"You will be of 100 years in: {Golden_Age}")