import smtplib
import datetime as dt
import random

sent = ""
now = dt.datetime.now()
wkday = now.weekday()

if wkday == 1:
    with open("Projects/D33_AutoMail/quotes.txt", "r") as quotes:
        quote = quotes.readlines()
        sent = random.choice(quote)
        print(sent)

    my_mail = 'pythoncode172@gmail.com'
    password = 'kmyqhhcmqsysczwa'
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs='piyushkr172@gmail.com', msg=f'Subject:Monday Motivation\n\n{sent}')
    connection.close()
else:
    print('it aint no monday')
