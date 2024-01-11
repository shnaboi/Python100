import requests
import os
from datetime import *

now = date.today()
today = now.strftime("%Y-%m-%d")
day_one = (now - timedelta(days=1)).strftime("%Y-%m-%d")
day_two = (now - timedelta(days=2)).strftime("%Y-%m-%d")
# print(today, day_one, day_two)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API_KEY = os.environ.get("AV_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

AV_PARAMS = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK,
  "apikey": AV_API_KEY
}

NEWS_PARAMS = {
  "q": "Tesla",
  # "country": "us",
  "apiKey": NEWS_API_KEY
}

stocks_response = requests.get(url='https://www.alphavantage.co/query?',
                               params= AV_PARAMS)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()
# print(stocks_data["Time Series (Daily)"][today])

def check_stocks():
  day_one_close = round(float(stocks_data["Time Series (Daily)"][day_one]['4. close']), 2)
  day_two_close = round(float(stocks_data["Time Series (Daily)"][day_two]['4. close']), 2)
  five_perc = (round(day_one_close * .01, 2) * 5)
  if day_one_close > day_two_close:
    if day_one_close - day_two_close > five_perc:
      print('Price went up more than 5%')
      get_news()
  elif day_two_close > day_one_close:
    if (day_two_close - day_one_close) > five_perc:
      print('Price went down more than 5%')
      get_news()
  else:
    print("Not enough significant change in stocks")

# check_stocks()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

news_response = requests.get(url='https://newsapi.org/v2/top-headlines?',
                             params=NEWS_PARAMS)
news_response.raise_for_status()
news_data = news_response.json()
# print(news_data["articles"][1]["url"])

def get_news():
  url_1 = news_data["articles"][0]["url"]
  url_2 = news_data["articles"][1]["url"]
  url_3 = news_data["articles"][2]["url"]
  print(f"{url_1}\n{url_2}\n{url_3}")

get_news()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

