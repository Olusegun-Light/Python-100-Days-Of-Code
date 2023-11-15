import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "api key"

account_sid = 'account key'
auth_token = 'auth token'

will_rain = False
weather_params = {
    "lat": 7.586500,
    "lon": 3.869880,
    "appid": api_key

}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]
# print(condition_code)

if int(condition_code) > 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_='+12055579353',
        to='+23409075690730'
    )
    print(message.status)



