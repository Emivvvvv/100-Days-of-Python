import datetime as dt
import random
import smtplib

#You should put you email and password directly to variables. I changed them with input fuction because I'll put my code on github to protect my mail address and pass.
my_email = input("Type your email address >>>")
password = input("Type your password >>>")
to_email = input("Type the email address which you want to send e pazartesi kirbaci >>>")

now = dt.datetime.now()
weekday = now.weekday()
hour = now.hour
second = now.second
send_once_checker = 0

with open("quotes.txt", "r") as quotes:
    quotes_list = quotes.readlines()
    quotes_list = [i[:-1] for i in quotes_list]


def weekly_quote():
    new_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Pazartesi kirbaci\n\n{new_quote}")
        connection.close()


if weekday == 0 and hour == 10 and second == 10:
    weekly_quote()