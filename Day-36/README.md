# Stock Price Monitoring and News Alert System

A Python script to monitor the stock prices of a specific company and send news alerts via SMS using Twilio.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system.
- Required Python libraries installed. You can install them using:

  ```bash
  pip install requests twilio
  ```

## Obtain API Keys

Before running the script, you need to obtain API keys for Alpha Vantage and News API. Follow the steps below to get your API keys:

### Alpha Vantage API Key

1. Visit the [Alpha Vantage website](https://www.alphavantage.co/).
2. Sign up for a free account or log in if you already have one.
3. Once logged in, navigate to the [API Key page](https://www.alphavantage.co/support/#api-key).
4. Follow the instructions to obtain your API key.

### News API Key

1. Visit the [News API website](https://newsapi.org/).
2. Sign up for a free account or log in if you already have one.
3. Once logged in, navigate to the [Get API Key page](https://newsapi.org/register).
4. Fill out the required information and submit the form.
5. After registration, you will receive your API key.

## Configuration

Before running the script, you need to configure the following settings in `main.py`:

1. **Twilio API Settings:**

   ```python
   TWILIO_SID = "Your Twilio SID"
   TWILIO_AUTH_TOKEN = "Your Twilio Auth Token"
   VIRTUAL_TWILIO_NUMBER = "Your Twilio Virtual Number"
   VERIFIED_NUMBER = "Your Verified Number"
   ```

   Replace the placeholders with your Twilio SID, Auth Token, Virtual Twilio Number, and Verified Number.

2. **Alpha Vantage and News API Keys:**

   ```python
   STOCK_API_KEY = "Your Alpha Vantage API Key"
   NEWS_API_KEY = "Your News API Key"
   ```

   Replace the placeholders with your Alpha Vantage and News API keys.

**Note**: Keep your API keys and sensitive information secure. Do not share them publicly.

## Usage

1. Run `main.py` to execute the script.
2. The script will fetch stock data, calculate the price difference, and send news alerts via Twilio.

## Acknowledgments

- This project uses the [Twilio API](https://www.twilio.com/) for sending SMS alerts.
- Stock data is fetched from [Alpha Vantage](https://www.alphavantage.co/).
- News data is obtained from the [News API](https://newsapi.org/).

Feel free to explore and modify the script based on your requirements. If you encounter any issues or have suggestions, please open an issue or contribute to the project.

Happy coding!
