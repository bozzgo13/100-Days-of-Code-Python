# Flash Card App - French to English

A functional Flash Card application built with Python and Tkinter. This project was developed as part of the **"100 Days of Code: The Complete Python Pro Bootcamp"** (Day 31).

## 🚀 Features
* **Dynamic Learning:** Randomly selects French words for the user to translate.
* **Auto-Flip Mechanism:** The card automatically flips to reveal the English translation after 3 seconds.
* **Progress Tracking:** Known words are removed from the list and saved to a `words_to_learn.csv` file, ensuring you only study words you haven't mastered yet.
* **Resilient Data Loading:** Automatically switches between the original dataset and your custom "to learn" list.

## 🛠️ Technologies Used
* **Python 3**
* **Tkinter:** For the Graphical User Interface (GUI).
* **Pandas:** For data manipulation and CSV handling.
* **Random:** For shuffling the flashcards.

## 📂 Project Structure
* `main.py`: The core logic and UI setup.
* `data/`: Contains `french_words.csv` (source) and `words_to_learn.csv` (progress).
* `images/`: Contains the UI assets (card backgrounds and buttons).

## 📝 How It Works
1.  **Start:** The app launches and shows a French word.
2.  **The Flip:** After 3 seconds, the card background changes and the English translation is displayed.
3.  **User Input:**
    * Click the **✔ (Right)** button if you knew the word. It will be removed from your future study list.
    * Click the **✖ (Wrong)** button if you didn't know it. The word will stay in the deck for later.
4.  **Persistent Storage:** Your progress is saved locally, so you can pick up where you left off.