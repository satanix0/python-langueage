import random
import smtplib
import pandas as pd
from datetime import datetime as dt
PLACEHOLDER = '[NAME]'
MY_MAIL = 'pythoncode172@gmail.com'
PASS = 'kmyqhhcmqsysczwa'


today = dt.now()
today_tup = (today.month, today.day)
print(today_tup)
data = pd.read_csv("Projects/D33_AutoMailBdayWish/birthdays.csv")
birthday_dict = {(drow["month"], drow["day"])                 : drow for (ind, drow) in data.iterrows()}

print(birthday_dict)


if today_tup in birthday_dict:
    person = birthday_dict[today_tup]
    filepath = f"Projects/D33_AutoMailBdayWish/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath, 'r') as file:
        filecont = file.read()
        newcont = filecont.replace(PLACEHOLDER, person["name"])

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASS)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=person["email"], msg=f'Subject:Happy Birthday\n\n{newcont}')
