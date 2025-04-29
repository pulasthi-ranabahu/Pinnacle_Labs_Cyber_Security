# 🖥️ Keylogger Software

The **Keylogger Software** script captures and logs every keystroke made on the keyboard to a file named `key_log.txt`.  
This tool is designed strictly for educational and security research purposes - **never use it on any system without explicit permission**.

**Project directory:**  
[https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security/tree/main/Keylogger_Software](https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security/tree/main/Keylogger_Software)

---

## 📦 Features

- **Logs all keystrokes** to a local file (`key_log.txt`)
- **Captures both regular and special keys** (Enter, Space, etc.)
- **Runs in the background** and stops when you press the `ESC` key
- **Simple, minimal, and beginner-friendly** Python code

---

## ⚙️ Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/pulasthi-ranabahu/Pinnacle_Labs_Cyber_Security
   cd Pinnacle_Labs_Cyber_Security/Keylogger_Software
   ```

2. **Install dependencies:**
   ```
   pip install pynput
   ```

---

## 💡 Usage

Run the script from the command line:

```
python keylogger.py
```

- The script will start logging all keystrokes to `key_log.txt` in the same directory.
- To stop the keylogger, press the **ESC** key.

---

## 🔍 How It Works

- The script uses the **pynput** library to listen for keyboard events.
- Every key press is appended to `key_log.txt`.
- **Special keys** (like Enter, Space, etc.) are recorded in a readable format.

---

## 🛠️ Troubleshooting

- **Permission denied / File not found:**  
  Make sure you have write permissions in the script directory.
- **ImportError:**  
  If you see errors like `Import "pynput" could not be resolved`, ensure you installed `pynput` with the correct Python interpreter and restart your editor.
- **Script doesn't stop:**  
  Only the **ESC** key will stop the script. If running in a terminal where `ESC` isn't captured, try another terminal or restart the shell.

---

## ⚠️ Disclaimer

This keylogger is designed **strictly for educational and research purposes**.  
**Do not use this tool on any system without explicit permission.**  
Misuse of keyloggers is illegal and unethical. Use responsibly to understand how keyloggers work and how to protect against them.

---

## 📄 License

This project is licensed under the MIT License.

---

**Make the most of your learning - build, understand, and secure! 🚀🔒**

---
