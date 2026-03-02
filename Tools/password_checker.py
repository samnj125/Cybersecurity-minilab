import re


def check_password_strength(password):
    score = 0
    if len(password) >= 12:  # len has been used to specify how many characters have been input
        score += 1
    # Here we use if to check if password has the right characters to be strong and adds/ removes score
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&+=!]", password):
        score += 1

# Here we cuse if and elif to check the sore and give feedback on the password

    if score <= 2:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    elif score <= 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength
