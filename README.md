# 🔐 Simple Ransomware Simulator (Educational Use Only)

> ⚠️ **DISCLAIMER:**  
> This project is intended **strictly for educational and awareness purposes**.  
> Do **NOT** use this tool for malicious purposes. Misuse can lead to serious legal consequences.  
> This simulator is designed to demonstrate how ransomware works so that users and developers can build better defenses.

---

## 📌 Project Overview

**Ransomware** is a type of malware that encrypts files and demands payment for their decryption. This simulator helps understand the basic mechanics of ransomware by encrypting files in a folder and allowing decryption using a saved key.

---

## 🎯 Objective

To simulate basic ransomware behavior in a safe and controlled environment:
- Encrypt files in a folder using symmetric encryption.
- Decrypt files using the saved key.
- Raise awareness about the importance of data security.

---

## 🛠️ Requirements

- Python 3.6+
- `cryptography` module (Install via pip)

```bash
pip install cryptography
📁 Folder Structure
bash
Copy
Edit
ransomware_simulator/
├── encryptor.py        # Script to encrypt files
├── decryptor.py        # Script to decrypt files
├── secret.key          # Saved encryption key (auto-generated)
└── target_files/       # Folder containing files to simulate ransomware attack
🚀 How to Use
1. Prepare Test Files
Place some sample files (e.g., .txt, .docx, .jpg) into the target_files/ folder.

2. Encrypt Files
Run the following script to encrypt all files inside the folder:

bash
Copy
Edit
python encryptor.py
A secret.key file will be generated.

Files in target_files/ will be encrypted and overwritten.

3. Decrypt Files
To decrypt the files, run:

bash
Copy
Edit
python decryptor.py
This uses the previously saved secret.key.

Files are restored to their original state.

🧠 How It Works
Uses Fernet encryption from the cryptography module.

A random symmetric key is generated once during encryption.

Encrypted files are overwritten — original content is not recoverable without the key.

The key is saved as secret.key and must be kept safe for successful decryption.

⚠️ Important Notes
Only encrypt non-critical, test files.

This is not real ransomware – no ransom is demanded.

Designed to promote understanding, not for exploitation.
