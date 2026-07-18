import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()")
    ]

    for _ in range(length - 4):
        password.append(random.choice(chars))

    random.shuffle(password)
    return "".join(password)


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()" for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


print("1. Generate Password")
print("2. Check Password Strength")

choice = input("Enter Choice (1/2): ")

if choice == "1":
    length = int(input("Enter Password Length: "))
    print("Generated Password:", generate_password(length))

elif choice == "2":
    password = input("Enter Password: ")
    print("Strength:", check_strength(password))

else:
    print("Invalid Choice")