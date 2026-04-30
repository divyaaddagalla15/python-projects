import re

def check_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8: score += 1
    else: remarks.append("Too short (min 8 chars)")

    if re.search(r"[A-Z]", password): score += 1
    else: remarks.append("Missing uppercase letter")

    if re.search(r"[0-9]", password): score += 1
    else: remarks.append("Missing numbers")

    if re.search(r"[@$!%*#?&]", password): score += 1
    else: remarks.append("Missing special character")

    return score, remarks

# Test
pwd = "Input_Password123!"
strength, feedback = check_password_strength(pwd)
print(f"Security Score: {strength}/4")
if feedback: print(f"Suggestions: {feedback}")
