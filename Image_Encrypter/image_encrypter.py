# image_encrypter.py

"""
Image Encrypter/Decrypter
-------------------------
Encrypt and decrypt image files using strong symmetric encryption (Fernet/AES).
This script is for educational and research purposes only.

Dependencies:
    pip install cryptography

Usage:
    python image_encrypter.py encrypt <input_image> <output_encrypted_file>
    python image_encrypter.py decrypt <input_encrypted_file> <output_image>

First, run the script with 'generate-key' to create a key:
    python image_encrypter.py generate-key

Keep the generated key file (key.key) safe! You need it for both encryption and decryption.
"""

import sys
from cryptography.fernet import Fernet

KEY_FILE = 'key.key'

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    print(f"Key generated and saved to '{KEY_FILE}'. Keep it safe!")

def load_key():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def encrypt_image(input_image, output_file):
    key = load_key()
    fernet = Fernet(key)
    with open(input_image, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(output_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"Image '{input_image}' encrypted and saved as '{output_file}'.")

def decrypt_image(input_file, output_image):
    key = load_key()
    fernet = Fernet(key)
    with open(input_file, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(output_image, 'wb') as dec_file:
        dec_file.write(decrypted)
    print(f"Encrypted file '{input_file}' decrypted and saved as '{output_image}'.")

def print_usage():
    print("""
Usage:
    python image_encrypter.py generate-key
    python image_encrypter.py encrypt <input_image> <output_encrypted_file>
    python image_encrypter.py decrypt <input_encrypted_file> <output_image>
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == 'generate-key':
        generate_key()
    elif command == 'encrypt' and len(sys.argv) == 4:
        encrypt_image(sys.argv[2], sys.argv[3])
    elif command == 'decrypt' and len(sys.argv) == 4:
        decrypt_image(sys.argv[2], sys.argv[3])
    else:
        print_usage()
