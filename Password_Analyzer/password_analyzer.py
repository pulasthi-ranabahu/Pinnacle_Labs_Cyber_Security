# password_analyzer.py

"""
Password Analyzer Script
-----------------------
Evaluates password strength and provides feedback and recommendations.

Usage:
    python password_analyzer.py
"""

import re
import string

def analyze_password(password):
    feedback = []
    score = 0

    # Length checks
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")
    elif len(password) < 12:
        feedback.append("Password could be longer for better security.")
        score += 1
    else:
        score += 2

    # Character type checks
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r'[{}]'.format(re.escape(string.punctuation)), password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, $, etc.).")

    # Strength assessment
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Okay"
    elif score == 4:
        strength = "Good"
    else:
        strength = "Strong"

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter your password for analysis: ")
    strength, feedback = analyze_password(password)
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Recommendations:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password is strong. Great job!")
