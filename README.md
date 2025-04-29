Here is a **general README.md** file for your Pinnacle Labs Cyber Security Internship repository.  
It covers all four main tasks, includes a troubleshooting section for import errors (as shown in your screenshot), and follows best practices for clarity and structure.

---

# 🛡️ Pinnacle Labs Cyber Security Internship 2025

Welcome to the official repository for the **Pinnacle Labs 2025 Cyber Security Internship Program**!  
This repository contains all the scripts and tools you need to complete your internship tasks and showcase your cybersecurity skills.

**Repository URL:**  
`https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security`

---

## 📚 Table of Contents

- [About](#about)
- [Features & Task List](#features--task-list)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting Import Errors](#troubleshooting-import-errors)
- [Submission Guidelines](#submission-guidelines)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📝 About

This repository is your one-stop resource for completing the Pinnacle Labs internship tasks.  
Each script is designed for practical learning, security research, and demonstration.  
You can use these tools individually or as part of a larger security toolkit.

---

## 🚀 Features & Task List

| Task               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Text Encryption    | Encrypt and decrypt text using AES, DES, and RSA algorithms.                |
| Keylogger Software | Track keystrokes and monitor user input for security research.              |
| Image Encryption   | Secure image files with encryption to protect visual data.                  |
| Password Analyzer  | Evaluate password strength and get recommendations for better security.      |

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

- Run any script from the command line. Example for the Text Encrypter:
  ```bash
  python Text_Encrypter.py
  ```
- Follow the interactive prompts for each tool.
- Check each script's README for detailed instructions and examples.

---

## 🛠️ Troubleshooting Import Errors

If you see warnings like  
`Import "cryptography.hazmat.primitives" could not be resolved`  
or  
`Import "Crypto.Cipher" could not be resolved`  
in VSCode or your terminal, follow these steps:

1. **Install the required packages**  
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

5. **Do not run import statements in PowerShell or CMD directly**  
   Only use them in a `.py` script or in the Python interactive shell (`python` command).

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
