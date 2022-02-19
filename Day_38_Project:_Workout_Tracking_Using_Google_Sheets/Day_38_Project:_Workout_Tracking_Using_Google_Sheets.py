import requests
import datetime

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 174
AGE = 19

APP_ID = "#"
API_KEY = "#"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

time = datetime.datetime.now()
date = time.strftime("%d/%m/%Y")
clock_time = time.strftime("%H:%M:%S")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

exercise = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
print(exercise, duration, calories)

sheety_endpoint = "https://api.sheety.co/#your endpoint"

headers = {
    "Authorization": "Bearer #####Your token"
}

new_row = {
    "workout": {
        "date": date,
        "time": clock_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

response = requests.post(url=sheety_endpoint, json=new_row, headers=headers)
response.raise_for_status()
