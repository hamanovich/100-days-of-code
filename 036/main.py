import requests
import os
from twilio.rest import Client

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

STOCK_NAME = "BTCUSDT"
COMPANY_NAME = "Bitcoin"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_response = requests.get(STOCK_ENDPOINT, params={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
})
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - \
    float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round(difference / float(yesterday_closing_price) * 100)

print(diff_percent)


if abs(diff_percent) > 0:
    news_response = requests.get(NEWS_ENDPOINT, params={
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    })
    articles = news_response.json()["articles"]
    last_three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadine: {article['title']}. \nBrief: {
        article['description']}" for article in last_three_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+12029524900",
            to="+XXX"
        )
