import math
import os
import requests
import datetime


#Stocks request
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK = "AYMSYNTEX"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}.BSE&outputsize=full&apikey={STOCK_API_KEY}"

response = requests.get(url)
response.raise_for_status()

#data
data = response.json()
dt = datetime.date.today() - datetime.timedelta(days=1)
previous_day_data = data["Time Series (Daily)"][str(dt)]
previous_day_open = previous_day_data["1. open"]
previous_day_close = previous_day_data["4. close"]

#percentage change
perct_change = math.floor((float(previous_day_close)-float(previous_day_open))*100/float(previous_day_open))
# print(perct_change)
if abs(perct_change) >= 5:
    print("Get News")
# print(previous_day_data["1. open"])


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
stock_name = STOCK.lower()
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
news_url = ('https://newsapi.org/v2/everything?'
       f'q=eros media&'
       f'from={dt}&'
       'sortBy=popularity&'
       f'apiKey={NEWS_API_KEY}')

news_response = requests.get(news_url)

data = news_response.json()
articles = data["articles"]
three_articles = articles[:2]
print(three_articles)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Same as done in day 35


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

