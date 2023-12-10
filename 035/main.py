import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

print(api_key)

weather_params = {
    "lat": 52.229675,
    "lon": 21.012230,
    "appid": api_key,
    "exclude": 'current,minutely,daily'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+12029524900",
        to="+48516450048"
    )
