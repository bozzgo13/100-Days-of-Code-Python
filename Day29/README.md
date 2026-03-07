# Password Manager GUI App 🔐

A desktop-based password management application built with **Python** and **Tkinter**. This app allows users to generate strong, random passwords and save their login credentials (website, email, and password) into a local text file for future reference.



## ✨ Features

* **Secure Password Generation:** Create complex passwords with a mix of letters, numbers, and symbols at the click of a button.
* **Data Persistence:** Saves your credentials in a structured format inside a `data.txt` file.
* **User-Friendly Interface:** A clean GUI featuring a logo, organized labels, and intuitive entry fields.
* **Validation & Alerts:** Includes error handling for empty fields and a confirmation popup before saving data.
* **Auto-Focus:** The cursor automatically starts in the "Website" field for a faster workflow.

## ⚠️ Security Warning (Usage Note)

> **IMPORTANT:** This application is created for **educational purposes only** as part of a programming challenge. 
> 
> * **No Encryption:** Passwords are saved in **plain text** within the `data.txt` file. 
> * **Not for Production:** This tool is **not suitable for actual use** to store sensitive real-world passwords, as anyone with access to your computer can read the file.

## 🛠️ Built With

* **Language:** Python 3
* **GUI Framework:** Tkinter
* **Libraries:** * `random` (for password logic)
    * `messagebox` (for user notifications)

## 📐 The Grid System (UI Layout)

To achieve a clean alignment, the application uses the `.grid()` geometry manager. The layout is structured as follows:

| Row | Column 0 | Column 1 | Column 2 |
| :--- | :--- | :--- | :--- |
| **0** | | Logo (Canvas) | |
| **1** | Website Label | Website Entry (Span 2) | |
| **2** | Email Label | Email Entry (Span 2) | |
| **3** | Password Label | Password Entry | Generate Button |
| **4** | | Add Button (Span 2) | |
