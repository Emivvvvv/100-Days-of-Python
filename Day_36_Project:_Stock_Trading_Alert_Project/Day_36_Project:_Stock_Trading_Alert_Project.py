import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = ""
api_key_news = ""

TWILITO_SID = ""
TWILITO_AUTH_TOKEN = ""
FROM_NUMBER = ""
TO_NUMBER = ""

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
diff_percent = (abs(difference) / float(yesterday_closing_price)) * 100
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
if diff_percent > 3:
    news_params = {
        "apiKey": api_key_news,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f'{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article["title"]}. \nBrief: {article["description"]}' for article in three_articles]

    client = Client(TWILITO_SID, TWILITO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )
    print(message.status)
