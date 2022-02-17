import requests
from datetime import datetime
import smtplib
import time


def is_it_night():
    if hour < sunrise or hour > sunset:
        return True
    else:
        return False


def location():
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LAT + 5:
        return True
    else:
        return False


MY_LAT = 40.974061
MY_LONG = 29.150975

#You should put you email and password directly to variables. I changed them with input fuction because I'll put my code on github to protect my mail address and pass.
my_email = "###########################"
password = "###########################"
to_email = "###########################"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour
second = time_now.second

print("Starting...")
time.sleep(1)
print("Everything works just fine!")
while True:
    time.sleep(30)
    if is_it_night() and location():
        print("ISS is top on your head a the moment!")
        print("Sending an email...")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:ISS is top on your head rn!\n\nDon't forget it is too fast so can be hard to catch!")
            connection.close()
