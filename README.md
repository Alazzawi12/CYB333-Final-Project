# CYB333-Final-Project
# Password Strength Analyzer

## Project Objectives

The **Password Strength Analyzer** is a Python-based tool designed to help users evaluate the strength of their passwords. It checks for common vulnerabilities such as:

- Use of frequently used passwords or dictionary words
- Sequential or repeated characters
- Keyboard patterns (e.g., `qwerty`, `123456`)
- Inadequate length or weak character variety

The program provides a strength rating from *Extremely Weak* to *Very Strong*, along with actionable suggestions to help users create more secure passwords.

---

## Features

- Detects common or overused passwords using a top 100,000 password list
- Flags weak patterns (e.g., `abc`, `qwerty`, `111`)
- Provides a score and security suggestions
- Simple command-line interface for real-time evaluation
- Checks for:
  - Password length
  - Use of upper/lowercase letters, digits, and symbols
  - Repeated or sequential characters
  - Keyboard layout patterns

---

## Setup Instructions

1. **Clone or download this repository.**

2. **Ensure you have Python installed.**  
   This project runs on Python.
3. Download or ensure the file 10-million-password-list-top-100000.txt is located in the same folder as the Python script.
4. Run the script

---
## Notes

1. If the password list is located elsewhere, update the file path in the load_common_words() function.
2. Passwords must be at least 6 characters long and contain at least one letter and one number.
3. The tool runs in a loop until the user types 'exit'.
4. This tool is built as part of a final project to promote better password hygiene through interactive feedback.

---

## License

This project is open-source and free to use for educational and personal security improvement purposes.
