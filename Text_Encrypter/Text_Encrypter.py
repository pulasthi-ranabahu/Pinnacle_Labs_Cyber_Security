import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# --- AES Encryption/Decryption ---
def derive_aes_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return kdf.derive(password.encode())

def aes_encrypt(plaintext: str, password: str) -> dict:
    salt = os.urandom(16)
    key = derive_aes_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return {
        'ciphertext': base64.b64encode(ciphertext).decode(),
        'salt': base64.b64encode(salt).decode(),
        'iv': base64.b64encode(iv).decode()
    }

def aes_decrypt(enc_dict: dict, password: str) -> str:
    salt = base64.b64decode(enc_dict['salt'])
    iv = base64.b64decode(enc_dict['iv'])
    ciphertext = base64.b64decode(enc_dict['ciphertext'])
    key = derive_aes_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()

# --- DES Encryption/Decryption ---
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def des_encrypt(plaintext: str, key: bytes) -> dict:
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text.encode())
    return {'ciphertext': base64.b64encode(ciphertext).decode()}

def des_decrypt(enc_dict: dict, key: bytes) -> str:
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = base64.b64decode(enc_dict['ciphertext'])
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode().rstrip()

# --- RSA Encryption/Decryption ---
def generate_rsa_keys():
    from cryptography.hazmat.backends import default_backend
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def rsa_encrypt(plaintext: str, public_key) -> str:
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode()

def rsa_decrypt(ciphertext_b64: str, private_key) -> str:
    ciphertext = base64.b64decode(ciphertext_b64)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# --- Main Menu ---
def main():
    while True:
        print("\nSelect algorithm:")
        print("1) AES")
        print("2) DES")
        print("3) RSA")
        print("4) Exit")
        algo = input("Enter choice: ").strip()

        if algo == '1':
            print("1) Encrypt\n2) Decrypt")
            choice = input("Enter choice: ").strip()
            if choice == '1':
                text = input("Enter text to encrypt: ")
                password = input("Enter password: ")
                enc = aes_encrypt(text, password)
                print("Encrypted:", enc)
            elif choice == '2':
                enc = {}
                enc['ciphertext'] = input("Enter base64 ciphertext: ")
                enc['salt'] = input("Enter base64 salt: ")
                enc['iv'] = input("Enter base64 iv: ")
                password = input("Enter password: ")
                try:
                    dec = aes_decrypt(enc, password)
                    print("Decrypted:", dec)
                except Exception as e:
                    print("Decryption failed:", e)
            else:
                print("Invalid choice.")

        elif algo == '2':
            print("1) Encrypt\n2) Decrypt")
            choice = input("Enter choice: ").strip()
            if choice == '1':
                text = input("Enter text to encrypt: ")
                key = get_random_bytes(8)
                print("DES Key (save this!):", base64.b64encode(key).decode())
                enc = des_encrypt(text, key)
                print("Encrypted:", enc)
            elif choice == '2':
                ciphertext = input("Enter base64 ciphertext: ")
                key_b64 = input("Enter base64 DES key: ")
                key = base64.b64decode(key_b64)
                enc = {'ciphertext': ciphertext}
                try:
                    dec = des_decrypt(enc, key)
                    print("Decrypted:", dec)
                except Exception as e:
                    print("Decryption failed:", e)
            else:
                print("Invalid choice.")

        elif algo == '3':
            print("1) Encrypt\n2) Decrypt")
            choice = input("Enter choice: ").strip()
            if choice == '1':
                text = input("Enter text to encrypt: ")
                priv, pub = generate_rsa_keys()
                enc = rsa_encrypt(text, pub)
                print("Encrypted:", enc)
                # Save private key for decryption
                priv_bytes = priv.private_bytes(
                    encoding = serialization.Encoding.PEM,
                    format = serialization.PrivateFormat.PKCS8,
                    encryption_algorithm = serialization.NoEncryption()
                )
                print("Private Key (save this!):\n", priv_bytes.decode())
            elif choice == '2':
                ciphertext = input("Enter base64 ciphertext: ")
                print("Paste your private key PEM (end with a blank line):")
                priv_pem_lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    priv_pem_lines.append(line)
                priv_pem = "\n".join(priv_pem_lines).encode()
                try:
                    priv = serialization.load_pem_private_key(priv_pem, password=None)
                    dec = rsa_decrypt(ciphertext, priv)
                    print("Decrypted:", dec)
                except Exception as e:
                    print("Decryption failed:", e)
            else:
                print("Invalid choice.")

        elif algo == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
