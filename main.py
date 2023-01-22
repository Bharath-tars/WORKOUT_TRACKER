import requests
import os
import datetime
dt = datetime.datetime.now()

NUTRI_ID = os.environ.get("NUTRI_ID")
NUTRI_KEY = os.environ.get("NUTRI_KEY")
SHEETY_KEY = os.environ.get("SHEETY_KEY")

EXERCICE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

hearder_exercise = {
"x-app-id": NUTRI_ID,
"x-app-key": NUTRI_KEY,
}

parameters_exercise ={
    "query": input("What shit you did? "),
    "gender":"male",
    "weight_kg":71.2,
    "height_cm":158.496,
    "age":19
}

responce = requests.post(url=EXERCICE_ENDPOINT, json=parameters_exercise, headers=hearder_exercise)
responce.raise_for_status()
exercise_data = responce.json()

SHEETY_ENDPOINT = 'https://api.sheety.co/826ce8befa9397d42fb73cbea164d933/myWorkoutsTars/workouts'
header_sheety={
"Authorization": SHEETY_KEY

}
parameters_sheety={
    "workout":{
    "date": dt.strftime(f"%d/%m/%Y"),
    "time": f"{dt.time().hour}:{dt.time().minute}:{dt.time().second}",
    "exercise": exercise_data["exercises"][0]['name'].title(),
    "duration": exercise_data["exercises"][0]['duration_min'],
    "calories": exercise_data["exercises"][0]["nf_calories"]
    }
}
responce_sheet = requests.post(url=SHEETY_ENDPOINT, json=parameters_sheety, headers=header_sheety)
print(responce_sheet.text)
