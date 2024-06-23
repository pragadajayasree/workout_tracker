import requests
from datetime import datetime
import os

app_id = os.environ["app_id"].strip().strip('"').strip("'")
api_key = os.environ["api_key"].strip().strip('"').strip("'")

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": 'application/json',
    "x-app-id": app_id,
    "x-app-key": api_key,
}

ex_text = input("which exercise did you do?")
weight = "54"
height = "162"
age = "19"
parameters = {
    "query": ex_text,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

response1 = requests.post(url=URL, json=parameters, headers=headers)
result = response1.json()

sheety_url = os.environ[
    "sheety_url"].strip().strip('"').strip("'")

current_date = datetime.now().strftime("%Y%m%d")
current_time = datetime.now().strftime("%X")
exercise = result["exercises"][0]["user_input"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
add_row = {
    "sheet1": {
        "date": current_date,
        "time": current_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

response2 = requests.post(url=sheety_url, json=add_row, auth=(os.environ["username"].strip().strip('"').strip("'"),
                                                          os.environ["password"].strip().strip('"').strip("'"),))
print(response2.text)
