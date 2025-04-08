def is_valid_password(password):
    if len(password) < 8 or len(password) > 16:
        return "Password must be 8-16 characters long."
    if not any(char in "%$#^&*!@()" for char in password):
        return "Password must have one special character (%$#^&*!@())."
    if not any(char.isdigit() for char in password):
        return "Password must have at least one number (0-9)."
    if not any(char.isupper() for char in password):
        return "Password must have at least one capital letter."
    if not password[0].islower():
        return "Password must start with a lowercase letter."
    if "pass" in password.lower() or "qwerty" in password.lower() or "123" in password:
        return "Password cannot contain 'pass', 'qwerty', or '123'."
    return "Valid"

print("Password rules:")
print("- Must be 8-16 characters")
print("- Must include one special character (%$#^&*!@())")
print("- Must include at least one number (0-9)")
print("- Must include at least one capital letter")
print("- Must start with a lowercase letter")
print("- Cannot include 'pass', 'qwerty', or '123'")

while True:
    user_password = input("\nEnter a password: ")
    result = is_valid_password(user_password)
    if result == "Valid":
        print("Success!")
        break
    else:
        print(f"Error: {result}")
