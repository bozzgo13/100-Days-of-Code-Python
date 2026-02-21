# Day 25: U.S. States Quiz Game

An interactive geography game built with Python. This project combines the `turtle` graphics library for the UI and `pandas` for data manipulation.

## 📝 Description
The goal of the game is to name all 50 U.S. states. When a user guesses correctly, the state's name appears on its actual geographical location on the map. If the user decides to quit, the program generates a list of the states they missed to help them study.

## 🚀 How to Play
1. Run the script.
2. Type the name of a U.S. State in the prompt window.
3. If correct, the name will appear on the map and your score will increase.
4. Type **"Exit"** to end the game and save your progress.

## 🛠️ Features
* **Real-time Map Updates:** Uses coordinates from a CSV file to place text on a GIF background.
* **Data Handling:** Utilizes `pandas` to read, filter, and extract data from a CSV.
* **Learning Tool:** Automatically generates `states_to_learn.csv` when you exit, listing all the states you haven't guessed yet.