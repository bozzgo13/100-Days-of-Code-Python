# Flight Club
This project represents the second part of the Flight Deal Finder capstone project. The goal of this stage is to upgrade the previous system by introducing a customer loyalty club ("Flight Club"), allowing new user registration and automatically broadcasting customized flight deal alerts via email to all registered members.

## 🚀 Project Overview

The application acts as an automated flight price monitor that tracks flights from a designated departure airport to various global destinations. When the system detects that a flight price has dropped below a pre-determined threshold (configured dynamically within a Google Sheet), it automatically compiles the flight details and distributes an alert to all club members.

### Key Features:
* **User Registration:** A console-based (or form-ready) interface to register new members (First Name, Last Name, and Email) directly into the database.
* **Data Management (Sheety API):** Seamless synchronization of both destination prices and user information with Google Sheets tabs.
* **Live Flight Scraping (SerpAPI):** Utilizes SerpAPI (Google Flights engine) to fetch up-to-the-minute flight prices, routes, and airline data.
* **Automated Broadcasting (SMTP):** Bulk email delivery using Python's `smtplib` to notify all registered users with formatted details (price, airports, dates, and transfer details).

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Core Libraries:** `requests`, `smtplib`, `datetime`
* **API Integrations:**
  * [SerpAPI](https://serpapi.com/) (Google Flights API for scraping live, accurate flight search results)
  * [Sheety API](https://sheety.co/) (For reading and writing to Google Sheets)

## 📁 Project Structure


```text
Day40/
│
├── main.py                 # Main entry point managing the core application loop
├── data_manager.py         # Handles communication with the Sheety API (Google Sheets)
├── flight_search.py        # Connects to SerpAPI to extract live flight information
├── flight_data.py          # Models flight structures, pricing thresholds, and stop-overs
├── notification_manager.py # Manages email layout compilation and SMTP broadcasting
└── README.md               # Project documentation

```

## ⚙️ Setup

### 1. Configure Google Sheets

Set up a Google Sheet with two distinct tabs:

1. **prices:** Columns: `City`, `IATA Code`, `Lowest Price`
2. **users:** Columns: `First Name`, `Last Name`, `Email`

Connect your sheet to Sheety to generate the respective API endpoints.

### 2. Environment Variables

For secure execution, configure the following environment variables in your system or within a local `.env` file:

```env
SERPAPI_API_KEY=your_serpapi_api_key
SHEETY_PRICES_ENDPOINT=[https://api.sheety.co/your_id/flightDeals/prices](https://api.sheety.co/your_id/flightDeals/prices)
SHEETY_USERS_ENDPOINT=[https://api.sheety.co/your_id/flightDeals/users](https://api.sheety.co/your_id/flightDeals/users)
SHEETY_USERNAME=username_for_basic_auth_to_sheety
SHEETY_PASSWORD=password_for_basic_auth_to_sheety
EMAIL_PROVIDER_SMTP_ADDRESS=smpt_address
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_email_password
TWILIO_AUTH_TOKEN=your_auth_token_from_twilio
TWILIO_SID=your_account_SID_from_twilio
TWILIO_VIRTUAL_NUMBER=sms_sender_number
TWILIO_WHATSAPP_NUMBER=whatsapp_sender_number
TWILIO_VERIFIED_NUMBER=sms_receiver_number
```

## 📈 Key Takeaways (Day 40)

* **Multi-Tab Data Relations:** Working with relational structures in no-code cloud databases via Sheety API.
* **Complex Business Logic:** Implementing fallback behaviors (searching for stop-over flights when direct connections yield no results).
* **Mass Communication:** Iterating through dynamic lists of recipients to broadcast personalized programmatic notifications via Python's `smtplib`.
* **Clean OOP Architecture:** Strengthening Object-Oriented Programming skills by maintaining distinct separation of concerns across dedicated modules.
