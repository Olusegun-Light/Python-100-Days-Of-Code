# Weather Alert System

This script checks the weather using the OpenWeatherMap API and sends an SMS alert using Twilio if rain is expected.

## Prerequisites

Before running the script, make sure you have the following:

- **OpenWeatherMap API Key**: Get your API key by signing up at [OpenWeatherMap](https://openweathermap.org/).
- **Twilio Account SID and Auth Token**: Sign up for a Twilio account at [Twilio](https://www.twilio.com/) to obtain your Account SID and Auth Token.
- **Twilio Phone Numbers**: Obtain the 'from\_' and 'to' phone numbers from your Twilio account.

## Setup

1. Install the required Python packages:

   ```bash
   pip install requests twilio
   ```

2. Replace the placeholder values in `main.py` with your actual API key and Twilio credentials.

```python
api_key = "your_openweathermap_api_key"

account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'

weather_params = {
    "lat": your_latitude,
    "lon": your_longitude,
    "appid": api_key
}

message = client.messages.create(
    body="It's going to rain today. Remember to bring an umbrella ☔",
    from_='your_twilio_phone_number',
    to='your_phone_number'
)
```

## Running the Script

Run the script using the following command:

```bash
python main.py
```

## Acknowledgments

- **OpenWeatherMap**: For providing accurate weather data. Visit their website [here](https://openweathermap.org/).

- **Twilio**: For the SMS alert service. Learn more [here](https://www.twilio.com/).

If you encounter any issues or have questions, feel free to reach out for assistance.
