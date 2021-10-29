import requests
from twilio.rest import Client
import os


MY_LAT = 41.8781
MY_LONG = -87.6298

API_KEY = os.environ.get("API_KEY")
OWM_ENDPOINT = os.environ.get("OWM_ENDPOINT")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
PHONE_NUMBER_TO = os.environ.get("PHONE_NUMBER_TO")

api_key = API_KEY
owm_endpoint = OWM_ENDPOINT
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
phone_number_to = PHONE_NUMBER_TO

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+18383843814',
        to=phone_number_to
    )
    print(message.status)

print("testing commit")



