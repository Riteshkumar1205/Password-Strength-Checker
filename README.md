## Password Strength Checker
**Welcome to the Password Strength Checker, a secure and intuitive desktop application designed to help users evaluate and enhance the strength of their passwords. Built with Python and Tkinter, this tool provides immediate feedback on password security and offers actionable recommendations for improvement.**

Key Features
Real-Time Analysis:
Receive instant feedback on your password’s strength as you type.

Strength Meter:
A visual progress bar clearly indicates whether your password is weak, moderate, or strong.

Comprehensive Feedback:
Get detailed suggestions to help you create a more secure password.

Security Checks:

Minimum Length: Enforces a minimum password length for enhanced security.

Character Diversity: Requires a mix of uppercase, lowercase, numbers, and special characters.

Pattern Detection: Identifies repeated or sequential characters.

Optional Dictionary Checks: Uses NLTK to detect common or dictionary-based passwords.

Breach Detection: Checks if your password has been exposed in known data breaches via the Have I Been Pwned (HIBP) API.

Password Visibility:
Toggle between showing and hiding your password for added convenience.


## 🌐 Repository
GitHub:
## https://github.com/RiteshKumar1205/password-strength-checker

## 🛠️ Installation & Running
🔹 Linux / macOS
Install Python 3 if not already installed.

Clone the repository:


**git clone https://github.com/RiteshKumar1205/password-strength-checker.git**
## Change Directory
 **cd password-strength-checker**
 
## Install dependencies:
**python3 -m pip install -r requirements.txt**

## Run the application:
**python3 main.py**

Or, for the command-line version:

bash
**python password_checker.py**

## 🔹 Windows
Install Python 3 if not already installed.

Clone the repository:

Open Command Prompt and run:

**git clone https://github.com/RiteshKumar1205/password-strength-checker.git**
## then
**cd password-strength-checker**

## Install dependencies:

text
**pip install -r requirements.txt**
## Run the application:


**python main.py**

## 💡 Optional: Dictionary Check Feature
To enable dictionary-based password checks using NLTK:

Run the setup script:

bash
python nltk_setup.py
This script will download the required NLTK corpus for dictionary word detection.

Restart the application to activate the dictionary check feature.

## How to Use: Step-by-Step Guide

Open the Application

**On Windows**: Double-click main.py or run python main.py in Command Prompt.

**On macOS/Linux:**  Run python3 main.py in Terminal.

Enter Your Password

Type your password in the provided field.

## Tip: On the command-line version, the password will be hidden as you type for security.



View Real-Time Feedback

Strength Meter: See a progress bar or color indicator showing password strength.

Detailed Suggestions: Get clear feedback on what makes your password weak or strong.

Breach Check: The tool will warn you if your password has been exposed in known data breaches.

Toggle Password Visibility (GUI Only)

Click the "Toggle Visibility" button to show or hide your password.

**Follow Recommendations**

If your password is weak, use the suggestions to improve it.

Optional: Use the built-in password generator for a strong password suggestion.

Repeat or Exit

You can check as many passwords as you like.

Press CTRL+C (command-line) or close the window (GUI) to exit.

Features in Detail
Minimum Length: Passwords must be at least 12 characters long for optimal security.

Character Complexity: Requires uppercase, lowercase, numbers, and special characters.

Pattern Detection: Identifies repeated or sequential characters and common sequences.

Dictionary Checks: (Optional) Detects if your password contains common dictionary words.

Breach Detection: Checks your password against the Have I Been Pwned API for exposure in data breaches.

Password Generation: (Optional) Generate strong passwords directly from the application.


## Contribution
We welcome contributions! If you have suggestions or improvements, please open an issue or submit a pull request.

