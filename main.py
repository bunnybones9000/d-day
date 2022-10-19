import datetime as dt
import random
import smtplib
my_email = "josefsho90@gmail.com"
password = "oxjwqyefxndqbbuf"

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as data:
    data_list = data.readlines()
    msg = random.choice(data_list)
    print(msg)

if now.weekday() == weekday:
    with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:hello\n\n {msg}")
