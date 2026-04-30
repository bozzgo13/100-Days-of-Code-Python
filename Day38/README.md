# Day 38: Workout Tracking using Google Sheets

This is a Python application that allows users to track their daily workouts using natural language processing. By simply typing what exercise they did (e.g., "I ran 5km and walked for 30 minutes"), the app calculates calories burned and duration, then automatically logs the data into a Google Sheet.

## 🚀 Features
- **Natural Language Processing**: Uses the nutrition API to understand exercise descriptions.
- **Automated Logging**: Integrates with the Sheety API to save workout data directly to Google Sheets.
- **Date & Time Tracking**: Automatically captures the current date and time for each entry.

## 🛠️ Prerequisites
Before running the script, you will need:
1. **100 Days of Python APIs**: Sign up at [100 Days of Python API](https://app.100daysofpython.dev/dashboard).
2. **Sheety API Key**: Create an account at [Sheety](https://sheety.co/) and connect your Google Sheet.
3. **Google Sheets**: A spreadsheet with headers: `Date`, `Time`, `Exercise`, `Duration`, `Calories`.

## ⚙️ Installation & Setup

1. Install the required dependencies:
   ```bash
   pip install requests
   ```

2. Set up your environment variables (recommended) or replace the placeholders in `main.py`:
   - `APP_ID`: Your 100 Days of Python API App ID
   - `API_KEY`: Your 100 Days of Python API Key
   - `WEIGHT_KG`: How much you weight in kg
   - `HEIGHT_CM`: Your height in cm
   - `AGE`: Your age
   - `GENDER`: Your gender (male/feemale)
   - `SHEETY_ENDPOINT`: Your Sheety project endpoint
   - `SHEETY_USERNAME`: Your Sheety username
   - `SHEETY_PASSWORD`: Your Sheety password
   
  
## 💻 Usage
Run the script:
```bash
python main.py
```
When prompted, describe your activity:
> *Example: "I ran for 2 km."*

The script will process the text and update your Google Sheet instantly.

## 📚 Technologies Used
- [Python 3](https://www.python.org/)
- [Requests Library](https://requests.readthedocs.io/)
- [100 Days of Python APIs](https://app.100daysofpython.dev/dashboard)
- [Sheety API](https://sheety.co/)
