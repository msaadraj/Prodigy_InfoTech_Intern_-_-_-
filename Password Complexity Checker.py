import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")

    if strength == 5:
        return "Strong Password ✅"
    elif strength >= 3:
        return "Moderate Password ⚠️\n" + "\n".join(feedback)
    else:
        return "Weak Password ❌\n" + "\n".join(feedback)

password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
