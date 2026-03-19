# Objective: send a motivational quote via email on the current weekday (currently set to Monday).
# Hints:
# 1. Use the datetime module to obtain the current day of the week.
# 2. Open the quotes.txt file and obtain a list of quotes.
# 3. Use the random module  to pick a random quote from your list of quotes.
# 4. Use smtplib to send the email to yourself.

import datetime as dt
import random
import smtplib

smtp_server = "smtp.gmail.com"
smtp_port = 587

my_email = "REAL_EMAIL@gmail.com" # replace with actual email
my_password = "abcd efgh ijkl mnop" # replace with actual password
receiver_email = "ANOTHER_REAL_EMAIL@gmail.com" # replace with actual email

now = dt.datetime.now()
day_of_week = now.weekday() # Monday == 0 ... Sunday == 6.

# Only send the email if today is Monday
if day_of_week == 0:
    try:
        # Attempt to open and read the file
        with open('quotes.txt', 'r') as file:
            quotes = file.readlines()

        # Check if the file is not empty to avoid errors with random.choice
        if quotes:
            random_quote = random.choice(quotes).strip()

            with smtplib.SMTP(host=smtp_server, port=smtp_port) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=receiver_email,
                    msg=f"Subject: Random quote\n\n{random_quote}"
                )

                print(f"A quote has been sent:\n{random_quote}")
        else:
            print("The file is empty.")

    except FileNotFoundError:
        print("Missing quotes file")
