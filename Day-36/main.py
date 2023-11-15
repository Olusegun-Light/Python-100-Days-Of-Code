import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# TWILIO_API = "https://www.twilio.com"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

STOCK_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "15min",
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_URL, stock_params)
Stock_data = stock_response.json()["Time Series (15min)"]
data_list = [value for (key, value) in Stock_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the absolute positive difference between yesterday and day before yesterday closing price
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = 0
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

# Work out the percentage difference in price between closing price and the day before yesterday
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"

# Get news if the percentage is greater than 5
if abs(diff_percent) < 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_URL, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [
        f"{COMPANY_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article, from_=VIRTUAL_TWILIO_NUMBER, to=VERIFIED_NUMBER
        )
