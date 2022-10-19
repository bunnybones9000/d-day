import pandas
import datetime as dt
##################### Extra Hard Starting Project ######################
now = dt.datetime.now()
month = now.month
day = now.day

bd = pandas.read_csv("birthdays.csv")
dates_month = (bd[bd.month])
dates_day = bd.day
# 1. Update the birthdays.csv
print(dates_month)
# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




