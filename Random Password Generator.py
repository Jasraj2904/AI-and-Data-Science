import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "!@#$%^&*_+-=?"
all_characters = letters + digits + special_characters
def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(all_characters)
    return password
length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(length))