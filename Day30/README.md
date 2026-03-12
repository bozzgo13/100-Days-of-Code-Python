# Password Manager +

An upgraded version of the Password Manager application (originally from Day 29 of the 100 Days of Code challenge). This version replaces the traditional flat-file `.txt` storage with a structured **JSON database**, enabling better data organization and efficient searching.

## Changes


* **JSON Data Storage:** Data is stored in `data.json`, making it structured and easy to read/parse.
* **Search Functionality:** Quickly retrieve saved credentials by searching for a specific website.
* **Error Handling:** * Handles missing data files (`FileNotFoundError`).
    * Notifies users if a website entry does not exist.
    * Prevents saving empty fields.
* **Improved UI:** A clean Tkinter interface with organized grid alignment.