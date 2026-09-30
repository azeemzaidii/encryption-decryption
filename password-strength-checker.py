password = input("Enter your password: ")

# Check password length
length = len(password)

# Check for numbers
has_number = any(char.isdigit() for char in password)

# Check for uppercase letters
has_uppercase = any(char.isupper() for char in password)

# Check for symbols
has_symbol = any(
    not char.isalnum() and not char.isspace()
    for char in password
)

# Decide password strength
if length < 8:
    strength = "Weak"
elif has_number and has_uppercase and has_symbol:
    strength = "Strong"
else:
    strength = "Medium"

# Display results
print("\nPassword Analysis")
print("-----------------")
print("Length:", length)
print("Contains number:", has_number)
print("Contains uppercase:", has_uppercase)
print("Contains symbol:", has_symbol)
print("Password Strength:", strength)