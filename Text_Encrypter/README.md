# 🛡️ Text Encrypter

This project is part of the Pinnacle Labs 2025 Cyber Security Internship Program.  
The **Text Encrypter** script allows you to securely encrypt and decrypt text using three major cryptographic algorithms: **AES**, **DES**, and **RSA**.

**Project directory:**  
[https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security/tree/main/Text_Encrypter](https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security/tree/main/Text_Encrypter)

---

## 📦 Features

- **AES Encryption/Decryption:** Secure text with password-based symmetric encryption.
- **DES Encryption/Decryption:** Classic symmetric encryption with a randomly generated key.
- **RSA Encryption/Decryption:** Asymmetric encryption using public/private key pairs.
- **Interactive CLI:** Choose your algorithm and operation (encrypt or decrypt) from a simple menu.

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security
   cd Pinnacle_Labs_Cyber_Security/Text_Encrypter
   ```

2. **Install dependencies:**
   ```bash
   pip install cryptography pycryptodome
   ```

---

## 💡 Usage

Run the script from the command line:

```bash
python Text_Encrypter.py
```

- Select the algorithm (**AES**, **DES**, or **RSA**).
- Choose to **encrypt** or **decrypt**.
- Follow the on-screen prompts to enter your text, password, or keys as needed.

---

## 🛠️ Troubleshooting Import Errors

If you see warnings like  
`Import "cryptography.hazmat.primitives" could not be resolved`  
or  
`Import "Crypto.Cipher" could not be resolved`  
in VSCode or your terminal, follow these steps:

1. **Install the required packages:**
   ```bash
   pip install cryptography pycryptodome
   ```

2. **Select the correct Python interpreter in VSCode:**
   - Click the Python version shown in the bottom bar of VSCode.
   - Choose the interpreter where you installed the packages (e.g., your virtual environment or system Python).

3. **Restart VSCode** after installing packages.

4. **Do not run Python import statements directly in PowerShell or CMD.**
   - Only use them in a `.py` script or inside the Python interactive shell (`python` command).

---

## 📄 License

This project is licensed under the MIT License.

---

**Make the most of your internship-learn, build, and secure! 🚀🔒**
