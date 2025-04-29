# Pinnacle_Labs_Cyber_Security
Text Encryption
# Text Encrypter Script

A cybersecurity project for encrypting and decrypting text using three major cryptographic algorithms: **AES**, **DES**, and **RSA**. This tool is designed for secure data protection and can be used as a learning resource or integrated into larger security solutions.

---

## Features

- **AES Encryption**: Secure symmetric encryption with password-based key derivation.
- **DES Encryption**: Classic symmetric encryption with an 8-byte key.
- **RSA Encryption**: Asymmetric encryption with public/private key pair generation.
- **Base64 Encoding**: Ensures encrypted output is safe for storage and transfer.
- **Command-Line Interface**: Simple, interactive prompts for ease of use.

---

## Requirements

- Python 3.7+
- [cryptography](https://pypi.org/project/cryptography/)
- [pycryptodome](https://pypi.org/project/pycryptodome/)

Install dependencies using:

```bash
pip install cryptography pycryptodome
```

---

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security
   cd text-encrypter
   ```

2. **Run the Script**

   ```bash
   python text_encrypter.py
   ```

3. **Follow the Prompts**

   - Choose the encryption algorithm (AES, DES, or RSA).
   - Enter the text to encrypt.
   - Enter a password (for AES) or use the generated key (for DES/RSA).
   - The script will display the encrypted and decrypted text.

---

## Example

```plaintext
Select algorithm: 1) AES 2) DES 3) RSA
Enter choice: 1
Enter text to encrypt: hello world
Enter password: mysecret
Encrypted: {'ciphertext': '...', 'salt': '...', 'iv': '...'}
Decrypted: hello world
```

---

## Security Notice

- This script is for educational and demonstration purposes.
- For production use, always follow best practices for key management and never share your encryption keys or passwords.
- DES is considered outdated and should not be used for sensitive data.

---

## Project Tasks (Internship Context)

This script fulfills the **Text Encryption** task for the Pinnacle Labs 2025 Internship Program.  
For other tasks (Keylogger, Image Encryption, Password Analyzer), see the project repository or contact the maintainer.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or support, please reach out via GitHub Issues or contact your internship coordinator.

---

**Happy Encrypting!**

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/64387307/6ccab0ea-b765-4d65-91ac-8c6bacb4436a/Cybersecurity_APR25P3.pdf

