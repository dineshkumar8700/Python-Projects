special_chars = set("[!@#$%^&*(),.?\":{}|<>]")

def password_strength_checker(password):
    if len(password) < 8:
        return "Very weak : Password Must contain at least 8 digit"
    if not any (char.isdigit() for char in password):
        return "Weak : Password must contain at least one digit"
    if not any (char.islower() for char in password):
        return "Weak : Password must contain at least one lowercase"
    if not any (char.isupper() for char in password):
        return "Weak : Password must contain at least one uppercase"
    if not any (char in special_chars for char in password):
        return "weak : Password must contain at least one special character"
    return "Strong password"

while True :
    password = input("Enter password : ")
    if password.lower() == "exit":
        print("Thankyou for using this tool")
        break
    strength = password_strength_checker(password)
    print(strength)


