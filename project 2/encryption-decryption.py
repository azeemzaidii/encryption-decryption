# Basic Encryption & Decryption using Caesar Cipher

def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


# Take input from user
text = input("Enter your text: ")
shift = int(input("Enter shift key: "))

# Encrypt the text
encrypted_text = encrypt(text, shift)

# Decrypt the text
decrypted_text = decrypt(encrypted_text, shift)

# Display results
print("\nEncryption & Decryption")
print("-----------------------")
print("Original Text :", text)
print("Shift Key     :", shift)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)