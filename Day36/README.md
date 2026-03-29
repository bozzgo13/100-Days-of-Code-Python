# Stock Trading News Alert 📈🗞️

This project is a Python-based automation tool developed as part of the **100 Days of Code: The Complete Python Pro Bootcamp**. It monitors stock price fluctuations and automatically sends SMS alerts containing relevant financial news when a significant price change occurs.

## 🚀 How it Works

1.  **Stock Monitoring:** Uses the **Alpha Vantage API** to fetch daily closing prices for a specific stock (e.g., Tesla).
2.  **Volatility Detection:** Compares the closing price of yesterday with the day before yesterday. If the difference is greater than **5%**, the script triggers a news search.
3.  **News Retrieval:** Uses the **News API** to fetch the top 3 most relevant articles about the company.
4.  **SMS Notification:** Sends a formatted SMS via the **Twilio API** detailing the price change (percentage and direction) along with the headlines and briefs of the news articles.

## 🛠️ Built With

  * **Python 3**
  * **Requests Library** (for API interactions)
  * **Alpha Vantage API** (Stock Market Data)
  * **News API** (Global News Data)
  * **Twilio API** (SMS Gateway)

## 📋 Prerequisites

Before running the script, you will need to obtain API keys from:

  * [Alpha Vantage](https://www.google.com/search?q=https://www.alphavantage.co/support/%23api-key)
  * [News API](https://newsapi.org/)
  * [Twilio](https://www.twilio.com/try-twilio)

## ⚙️ Setup

1.  **Environment Variables:**
    To keep your credentials secure, replace the placeholders in `main.py` (or use a `.env` file) with your actual data:

      * `STOCK_NAME`: The ticker symbol (e.g., `TSLA`)
      * `COMPANY_NAME`: The name of the company (e.g., `Tesla Inc`)
      * `STOCK_API_KEY`: Your Alpha Vantage key
      * `NEWS_API_KEY`: Your News API key
      * `TWILIO_SID`: Your Twilio Account SID
      * `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token

2.  **Run the application:**

    ```bash
    python main.py
    ```

## 📱 Example Output

When the stock moves significantly, you will receive an SMS like this:

```text
TSLA: 🔺5.2%
Headline: Why Tesla Stock Is Climbing Today.
Brief: Shares of Tesla (TSLA) rose following a positive delivery report...

Headline: Elon Musk announces new Gigafactory location.
Brief: Tesla CEO Elon Musk confirmed today that the company will expand...
```