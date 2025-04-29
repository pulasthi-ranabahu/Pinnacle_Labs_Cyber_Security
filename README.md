Here is an updated `README.md` file for your repository, **including a troubleshooting section for import errors** like those shown in your screenshot. This will help users resolve common issues with missing Python packages in VSCode and ensure your internship project is easy to set up and use.

---

# 🛡️ Pinnacle Labs Cyber Security Internship 2025

Welcome to the official repository for the **Pinnacle Labs 2025 Cyber Security Internship Program**!  
This repo contains all the project scripts and tools you need to complete your internship tasks and showcase your cybersecurity skills.

**Repository URL:**  
`https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security`

---

## 📚 Table of Contents

- About
- Features
- Installation
- Usage
- Troubleshooting Import Errors
- Internship Tasks
- Submission Guidelines
- Contributing
- License
- Contact

---

## 📝 About

This repository is your one-stop resource for completing the Pinnacle Labs internship tasks.  
Each script is designed for practical learning, security research, and demonstration.  
You can use these tools individually or as part of a larger security toolkit.

---

## 🚀 Features

- **Text Encryption**: Encrypt and decrypt text using AES, DES, and RSA.
- **Keylogger Software**: Research tool for monitoring keystrokes and understanding keylogger threats.
- **Image Encryption**: Secure image files to protect visual data.
- **Password Analyzer**: Evaluate and improve password strength.

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security
   cd Pinnacle_Labs_Cyber_Security
   ```

2. **Install dependencies:**
   ```bash
   pip install cryptography pycryptodome
   ```
   *Each script may have additional dependencies; see individual script READMEs for details.*

---

## 💡 Usage

Run any script from the command line. For example, to use the Text Encrypter:

```bash
python Text_Encrypter.py
```

Follow the interactive prompts for each tool.  
Check each script's README for detailed instructions and examples.

---

## 🛠️ Troubleshooting Import Errors in VSCode

If you see warnings like  
`Import "cryptography.hazmat.primitives" could not be resolved`  
or  
`Import "Crypto.Cipher" could not be resolved`  
please follow these steps:

1. **Install the required packages**  
   Open your terminal and run:
   ```bash
   pip install cryptography pycryptodome
   ```

2. **Select the correct Python interpreter in VSCode**  
   - Click the Python version shown in the bottom bar of VSCode.
   - Choose the interpreter where you installed the packages (e.g., your virtual environment or system Python).

3. **Restart VSCode**  
   Sometimes VSCode needs to be restarted to recognize new packages.

4. **Test your imports**  
   Open a terminal and run:
   ```bash
   python
   ```
   Then type:
   ```python
   from cryptography.hazmat.primitives.ciphers import Cipher
   from Crypto.Cipher import DES
   ```
   If you see no errors, your environment is set up.

5. **Still having issues?**  
   - Make sure you are not running import statements directly in PowerShell or CMD.  
   - Only run them in a `.py` script or in the Python interactive shell (`python` command).

---

## 🏆 Internship Tasks

| Task               | Description                                            |
|--------------------|-------------------------------------------------------|
| Text Encryption    | Encrypt text with AES, DES, RSA                       |
| Keylogger Software | Research tool for keystroke monitoring                |
| Image Encryption   | Secure image files with encryption algorithms         |
| Password Analyzer  | Analyze and improve password security                 |

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!  
Fork the repo, create a pull request, or open an issue for feedback.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

For questions or support, open an issue or reach out to your internship coordinator.

---

**Make the most of your internship-learn, build, and secure! 🚀🔒**
