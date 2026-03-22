# ISS Overhead Notifier & API Fundamentals

This repository contains the projects and exercises completed during Day 33 of the **100 Days of Code**. The primary focus of this day was learning how to interact with **External APIs (Application Programming Interfaces)**, handling JSON data, and understanding API parameters.

## 🛰️ Main Project: ISS Overhead Notifier

The **ISS Overhead Notifier** is an automated Python script that monitors the current location of the International Space Station (ISS) relative to the user's position.

### Features
- **Real-time Tracking:** Uses the Open Notify API to fetch the current latitude and longitude of the ISS.
- **Solar Position Logic:** Uses the Sunrise-Sunset API to determine if it is currently dark at the user's location.
- **Automated Alerts:** If the ISS is directly overhead (within +/- 5 degrees of latitude and longitude) and it is nighttime, the script sends an email notification to the user, telling them to look up.

### How it Works
1. **API Requests:** The script sends GET requests to the ISS location API and the Sunrise-Sunset API.
2. **Coordinate Comparison:** It compares the ISS coordinates with the hardcoded `MY_LAT` and `MY_LONG`.
3. **Time Verification:** It checks the current hour against the sunrise and sunset hours of the user's location.
4. **Email Trigger:** If both conditions (location and darkness) are met, it uses the `smtplib` module to send an alert.

### Setup Requirements
- Python 3.x
- `requests` library
- A valid email account (and App Password for Gmail users) to send notifications.

---

## 📝 Learning Exercises

In addition to the main project, the following exercises were completed to master the basics of API interaction:

### Exercise 1: ISS Location Tracker
A basic introduction to the `requests` module.
- Learned how to fetch data from `http://api.open-notify.org/iss-now.json`.
- Practiced handling HTTP response codes (e.g., 200, 404, 401).
- Extracted specific data (latitude/longitude) from the returned JSON object.

### Exercise 2: Kanye Quotes App
A fun GUI-based application using the `tkinter` library.
- Integrated the **Kanye.rest API**.
- Implemented a function that fetches a random quote and updates the UI text whenever a button is pressed.
- Focused on parsing JSON keys and updating dynamic GUI elements.

### Exercise 3: Sunrise & Sunset Times
An exercise focused on **API Parameters**.
- Learned how to pass specific data (latitude, longitude, and `formatted` settings) into an API call using the `params` argument.
- Worked with the Sunrise-Sunset API to retrieve UTC times.
- Practiced string splitting and data type conversion to extract the hour from an ISO 8601 formatted string.
