##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import pandas as pd
import datetime as dt
import smtplib
import random
import os

MY_EMAIL = "REAL_EMAIL@gmail.com" # replace with actual email
MY_PASSWORD = "abcd efgh ijkl mnop" # replace with actual password
TEMPLATES_DIR = "letter_templates"

# Check Current Date
today = dt.datetime.now()

# Load birthdays data
data = pd.read_csv("birthdays.csv")

# Create a dictionary of birthdays
# (month, day): row_data
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today's date exists in our dictionary
if (today.month, today.day) in birthdays_dict:
    birthday_person = birthdays_dict[(today.month, today.day)]

    # Pick a random letter template
    file_list = os.listdir(TEMPLATES_DIR)
    random_letter = random.choice(file_list)

    # 6. Read and replace the [NAME] placeholder
    with open(f"{TEMPLATES_DIR}/{random_letter}") as letter_file:
        content = letter_file.read()
        final_message = content.replace("[NAME]", birthday_person["name"])

    # Send the Email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{final_message}"
        )
    print(f"Birthday email sent to {birthday_person['name']}!")
else:
    print("No birthdays to celebrate today.")
