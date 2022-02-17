import requests
from twilio.rest import Client

#You should put your api key, acoount sid and auth token directly to variables. I changed them with input fuction because I'll put my code on github to protect my mail address and pass.
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = input("Your api key >>>")
account_sid = input("Your account sid >>>")
auth_token = input("Your auth token >>>")
from_phone = input("Your from phone >>>")
to_phone = input("Your to phone >>>")
will_rain = False

weather_params = {
    "lat": 40.974015,
    "lon": 29.151008,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    else:
        will_rain = False

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=from_phone,
        to=to_phone,
    )
    print(message.status)