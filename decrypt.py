import os
from cryptography.fernet import Fernet

# Load the saved key
def load_key():
    return open("secret.key", "rb").read()

# Decrypt a single file
def decrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

# Decrypt all files in the folder
def decrypt_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            decrypt_file(file_path, key)
            print(f"Decrypted: {file_path}")

if __name__ == "__main__":
    folder = "target_files"
    key = load_key()
    decrypt_folder(folder, key)
    print("\nAll files decrypted successfully.")
