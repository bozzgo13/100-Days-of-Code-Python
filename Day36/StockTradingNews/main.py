import requests
import os
import math
from dotenv import load_dotenv
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

load_dotenv() # Load variables from the .env file into the system environment

## STEP 1: Use https://www.alphavantage.co
# Get your real API key at https://www.alphavantage.co/support/#api-key
API_KEY = os.getenv('API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)

response.raise_for_status()
response_Json = response.json() # Good JSON viewer is at https://jsonviewer.stack.hu/
days = response_Json["Time Series (Daily)"]
days_as_list = list(days.values())
keys = list(days.keys())


yesterday =  days_as_list[0]
yesterday_key =  keys[0]
yesterday_close = float(yesterday["4. close"])
day_before_yesterday =  days_as_list[1]
day_before_yesterday_key =  keys[1]
day_before_yesterday_close =  float(day_before_yesterday["4. close"])
difference = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100
abs_diff = abs(difference)

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if abs_diff  >= 5:
    print("Get News")

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "from": keys[0],
        "to": keys[1],
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }

    response2 = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    response2.raise_for_status()
    response2_Json = response2.json()
    articles = response2_Json["articles"][:3]

    # Credentials from the Twilio Console
    account_sid = os.getenv('TWILIO_API_KEY')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_SENDER_NUMER')  # Your Twilio phone number
    receiver_number = os.getenv('TWILIO_RECEIVER_NUMER')

    client = Client(account_sid, auth_token)

    icon = "🔺" if difference > 0 else "🔻"
    ## STEP 3: Use https://www.twilio.com
    # Send a separate messages with the percentage change and each article's title and description to your phone number.
    for article in articles:
        # Optional: Format the SMS message like this:
        """
        TSLA: 🔺2%
        Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
        or
        "TSLA: 🔻5%
        Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
        """
        msg_body = (
            f"{STOCK}: {icon}{abs_diff:.2f}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )
        message = client.messages.create(
            from_=twilio_number,
            body=msg_body,
            to=receiver_number
        )
        print(f"Message sent successfully! SID: {message.sid}")
