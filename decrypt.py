import os
from cryptography.fernet import Fernet

# Load the encryption key from the key file
with open('thekey.key', 'rb') as key_file:
    key = key_file.read()

# Creating a Fernet object with the loaded key
cipher = Fernet(key)

# List all files in the directory
files = os.listdir()

# Decrypt each file
for file in files:
    if file == 'thekey.key' or file == 'script.py' or file == '.idea' or file == 'decrypt.py' or file == '.git':
        continue

    with open(file, 'rb') as f:
        encrypted_data = f.read()

    decrypted = Fernet(key).decrypt(encrypted_data)

    with open(file, 'wb') as f:
        f.write(decrypted)

print("Decryption done")
