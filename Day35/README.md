# Rain Alert SMS Notifier 🌧️📱

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp**. It automatically checks the weather forecast for a specific location and sends an SMS notification via **Twilio** if rain is predicted in the next 12 hours.

## 🚀 Features
* Fetches 48-hour weather forecast data using the **OpenWeatherMap API**.
* Filters data to check for rain-related weather codes.
* Sends a real-time SMS alert to your phone using the **Twilio API**.
* Uses environment variables to keep sensitive API keys secure.

## 🛠️ Prerequisites

Before running the script, ensure you have the following:
* **Python 3.x** installed.
* An **OpenWeatherMap** account (to get your `OWM_API_KEY`).
* A **Twilio** account (to get your `AUTH_TOKEN`, `ACC_SID`, and a Twilio phone number).
* A verified phone number in Twilio (if using a trial account).

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/bozzgo13/100-Days-of-Code-Python.git](https://github.com/bozzgo13/100-Days-of-Code-Python.git)
    cd 100-Days-of-Code-Python/Day35/RainAlert
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # Activate on Windows:
    .\venv\Scripts\activate
    # Activate on macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the required library:**
    ```bash
    pip install twilio requests
    ```

## ⚙️ Configuration

To keep your credentials safe, this project uses environment variables. You can set them up in your terminal or use a `.env` file:

| Variable | Description |
| :--- | :--- |
| `OWM_API_KEY` | Your OpenWeatherMap API Key |
| `TWILIO_ACCOUNT_SID` | Your Twilio Account SID |
| `TWILIO_AUTH_TOKEN` | Your Twilio Auth Token |
| `TWILIO_VIRTUAL_NUMBER` | Your Twilio assigned phone number |
| `MY_PHONE_NUMBER` | Your personal phone number (recipient) |

## 🖥️ Usage

Run the script using:
```bash
python main.py
```

## ⚠️ Security Note
**Never commit your actual API keys or Tokens to GitHub.** This project is configured to use environment variables to prevent sensitive data leaks. Ensure your `.env` file is added to your `.gitignore`.
