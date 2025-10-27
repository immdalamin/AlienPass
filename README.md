# 👽 AlienPass - Secure Password Generator

A simple, customizable Python script for generating strong, random passwords from the command line.

***

## 🚀 About AlienPass

In an age of constant security threats, strong passwords are non-negotiable. **AlienPass** is a command-line utility written in Python that provides a quick and customizable way to generate secure, cryptographically random passwords based on your specific requirements.

It guides you through setting the password parameters and ensures the generated passwords are saved safely to a dedicated, timestamped file for easy retrieval.

---

## ✨ Features

* **Custom Length:** Generate passwords from **8 to 20** characters long.
* **Character Inclusion:** Option to include **uppercase letters** (A-Z) and **symbols** (`!@#$%^&*` etc.).
* **Readability:** Option to **exclude confusing characters** (e.g., 'O', '0', 'I', 'l') to prevent transcription errors.
* **Bulk Generation:** Generate multiple passwords in a single run.
* **Automatic Saving:** Passwords are automatically saved to a timestamped text file for safe keeping.

---

## ⚙️ Setup and Prerequisites

AlienPass requires **Python 3.x**. No external libraries are needed as it uses standard built-in modules (`random`, `string`, `os`, `datetime`).

### Installation and Running

1.  **Clone or Download:** Use git to clone the repository or download the source code:

    ```bash
    git clone https://github.com/immdalamin/AlienPass/
    cd AlienPass
    ```

2.  **Run:** Open your terminal or command prompt, navigate to the directory where you saved the file (if you cloned it, you're already in the `AlienPass` directory), and execute the script:

    ```bash
    python AlienPass.py
    ```

---

## 📋 Example Usage

The script is interactive and will prompt you for all necessary settings upon execution:
