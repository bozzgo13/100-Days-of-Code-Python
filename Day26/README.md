# NATO Alphabet Project

A Python-based tool that converts any word provided by the user into its corresponding **NATO Phonetic Alphabet** code words. This project demonstrates the use of **Pandas** for data manipulation and **list comprehension** for efficient data processing.



## 🚀 Features
* **Data Integration:** Reads phonetic data directly from a CSV file using the Pandas library.
* **Dictionary Comprehension:** Efficiently maps alphabet letters to their phonetic equivalents.
* **Error Handling:** Includes a `try-except-else` block to handle non-alphabetic characters gracefully, ensuring the program doesn't crash on invalid input.
* **User Interaction:** Simple command-line interface for quick translations.

---

## 🖥️ How It Works
1. The program loads the `nato_phonetic_alphabet.csv` file.
2. It converts the CSV data into a Python dictionary format: `{"A": "Alfa", "B": "Bravo", ...}`.
3. The user is prompted to enter a word.
4. The program iterates through the word and prints a list of the phonetic codes.

---

## 💻 Example Output
```text
Enter a word: Bostjan
['Bravo', 'Oscar', 'Sierra', 'Tango', 'Juliet', 'Alfa', 'November']
```

