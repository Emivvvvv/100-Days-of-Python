import pandas
import datetime as dt
import smtplib
import random

#You should put you email and password directly to variables. I changed them with input fuction because I'll put my code on github to protect my mail address and pass.
my_email = input("Type your email address >>>")
password = input("Type your password >>>")

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
day = now.day

for i in range(0, len(data["month"])):
    if month == data["month"][i] and day == data["day"][i]:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
            letter_contents = letter.read()
            new_letter = letter_contents.replace("[NAME]", data["name"][i])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=data["email"][i],
                                msg=f"Subject:Happy Birthday!\n\n{new_letter}")
            connection.close()