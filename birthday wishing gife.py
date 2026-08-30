password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(not char.isalnum() for char in password):
    score += 1

if score <= 2:
    print("Password strength: Weak ❌")
elif score <= 4:
    print("Password strength: Medium ⚠️")
else:
    print("Password strength: Strong ✅")