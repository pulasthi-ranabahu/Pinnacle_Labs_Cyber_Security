# 🖼️ Image Encrypter

The **Image Encrypter** script allows you to securely encrypt and decrypt image files (such as JPG, PNG, etc.) using strong symmetric encryption with the `cryptography` library (Fernet/AES).  
This tool is designed for educational and security research purposes-**never use it on any system without explicit permission**.

**Project directory:**  
[https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security/tree/main/Image_Encrypter](https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security/tree/main/Image_Encrypter)

---

## 📦 Features

- **Encrypt any image file** (JPG, PNG, etc.) with strong symmetric encryption (Fernet/AES)
- **Decrypt encrypted image files** back to their original form
- **Simple command-line usage** for both encryption and decryption
- **Key generation and management**-keep your key file (`key.key`) safe!

---

## ⚙️ Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security
   cd Pinnacle_Labs_Cyber_Security/Image_Encrypter
   ```

2. **Install dependencies:**
   ```
   pip install cryptography
   ```

---

## 💡 Usage

**1. Generate a key (do this once and keep the key file safe):**
```
python image_encrypter.py generate-key
```

**2. Encrypt an image:**
```
python image_encrypter.py encrypt input.jpg encrypted.img
```

**3. Decrypt an image:**
```
python image_encrypter.py decrypt encrypted.img output.jpg
```

- The script will create a `key.key` file in the same directory.  
- You must keep this key file safe; without it, you cannot decrypt your images.

---

## 🔍 How It Works

- The script uses the `cryptography` library’s Fernet implementation (AES-based) for secure, symmetric encryption.
- The `key.key` file is required for both encryption and decryption.
- Any binary image file can be encrypted and decrypted without loss.

---

## 🛠️ Troubleshooting

- **Permission denied / File not found:**  
  Make sure you have read/write permissions in the script directory and that the file paths are correct.
- **ImportError:**  
  If you see errors like `Import "cryptography" could not be resolved`, ensure you installed `cryptography` with the correct Python interpreter and restart your editor.
- **Lost key file:**  
  If you lose `key.key`, you will not be able to decrypt your images. Always keep a backup of your key file.

---

## ⚠️ Disclaimer

This image encrypter is designed **strictly for educational and research purposes**.  
**Do not use this tool on any system or with any data without explicit permission.**  
Misuse of encryption tools may be illegal or unethical. Use responsibly to understand how encryption works and how to protect your data.

---

## 📄 License

This project is licensed under the MIT License.

---

**Make the most of your learning-build, understand, and secure! 🚀🔒**
