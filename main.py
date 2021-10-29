import requests
from twilio.rest import Client
import os


MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")


API_KEY = os.environ.get("API_KEY")
OWM_ENDPOINT = os.environ.get("OWM_ENDPOINT")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
PHONE_NUMBER_TO = os.environ.get("PHONE_NUMBER_TO")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella.",
            from_='+18383843814',
            to=PHONE_NUMBER_TO
    )
    print(message.status)





