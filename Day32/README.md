# 🎂 Automated Birthday Wisher

A Python-based automation tool that monitors a CSV file of birthdays, picks a randomized greeting from a template folder, and sends a personalized email to the birthday person automatically.

## 🚀 Features
* **Pandas Integration**: Efficiently parses birthday data from a CSV file.
* **Randomized Messaging**: Picks a random template from a pool of letters to keep greetings fresh.
* **Dynamic Placeholders**: Automatically replaces `[NAME]` with the recipient's actual name.
* **Secure Delivery**: Uses SMTP with TLS encryption to send emails via Gmail.

## 📂 Project Structure
```text
.
├── main.py                # The main Python script
├── birthdays.csv          # Data file (name,email,year,month,day)
├── letter_templates/      # Folder containing your .txt letter templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── ...
└── README.md
```

## 🛠️ Setup & Requirements

### 1. Prerequisites
You will need **Python 3.x** and the **pandas** library installed:
`pip install pandas`

### 2. Prepare the CSV
Ensure your `birthdays.csv` follows this exact format:
```csv
name,email,year,month,day
John Doe,john@example.com,1990,12,25
```

### 3. Letter Templates
Create a folder named `letter_templates` and add `.txt` files. Inside the files, use the placeholder **`[NAME]`**.

### 4. Gmail Authentication
1. Enable **2-Step Verification** in Google account.
2. Create **App Password**.
3. Copy code in `MY_PASSWORD`.

## 🖥️ Usage
Update `MY_EMAIL` and `MY_PASSWORD` in `main.py`, and run:
`python main.py`

## 🐧 Automation on Linux (Cron Job)

To make the script run automatically every day on a Linux server (like Ubuntu, Debian, or Raspberry Pi), we use the **Cron** utility.

### 1. Find your Python path
First, you need to know where your Python is installed. Run this in your terminal:
```bash
which python3
```
*Example output: `/usr/bin/python3`*

### 2. Find your Script path
Get the full path to your `main.py` file:
```bash
readlink -f main.py
```
*Example output: `/home/username/birthday-wisher/main.py`*

### 3. Set up the Cron Job
Open the crontab editor:
```bash
crontab -e
```

Add the following line at the very bottom of the file to run the script every day at **09:00 AM**:

```bash
00 09 * * * /usr/bin/python3 /home/username/birthday-wisher/main.py >> /home/username/birthday-wisher/log.txt 2>&1
```



### Breakdown of the Cron Command:
* `00 09 * * *`: Runs at minute 0, hour 9 (9:00 AM), every day, every month, every weekday.
* `/usr/bin/python3`: The absolute path to your Python interpreter.
* `/home/.../main.py`: The absolute path to your script.
* `>> .../log.txt 2>&1`: This part is optional but recommended; it saves any output or errors to a `log.txt` file so you can check if it worked.

### 4. Verify
To see your active cron jobs, run:
```bash
crontab -l
```

## 🪟 Automation on Windows (Task Scheduler)

To ensure your birthday wisher runs every morning without manual intervention, you can use the built-in **Windows Task Scheduler**.

### 1. Locate your Python Executable
Open your **Command Prompt** (cmd) and type:
```cmd
where python
```
*Example path: `C:\Users\YourName\AppData\Local\Programs\Python\Python310\python.exe`*

### 2. Create a Batch File (`.bat`)
A batch file acts as a shortcut that Windows can trigger easily. Create a new file in your project folder named `run_birthday.bat` and paste the following (update the paths to match your computer):

```batch
@echo off
"C:\Path\To\Your\python.exe" "C:\Path\To\Your\Project\main.py"
pause
```
> **Note:** The `pause` command keeps the window open so you can see if the email sent successfully. Once you are sure it works, you can remove `pause` for a completely silent run.

### 3. Configure Task Scheduler
1. Press the **Windows Key**, type **"Task Scheduler"**, and hit **Enter**.
2. In the right-hand **Actions** pane, click **Create Basic Task...**.
3. **Name**: `BirthdayWisher`. Click **Next**.
4. **Trigger**: Select **Daily**. Click **Next**.
5. **Daily**: Set the **Start Time** (e.g., 09:00:00). Click **Next**.
6. **Action**: Select **Start a program**. Click **Next**.
7. **Program/script**: Click **Browse** and select your `run_birthday.bat` file.
8. **Finish**: Click **Finish**.
