import datetime as dt
import random
import pandas
import smtplib

my_email = "josefsho90@gmail.com"
password = "oxjwqyefxndqbbuf"

num = random.randint(1, 3)
# 2. Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month, dt.datetime.now().day)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")



birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
print(data)
"""
if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{num}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthdays_person["email"],
        msg=f"Subject:Happy birthday\n\n {content}")
"""