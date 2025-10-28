# code by Md. Al-Amin
import random
import string
import os
from datetime import datetime

banner = r"""
=====================================================================
   _____  .__  .__                __________                       
  /  _  \ |  | |__| ____   ____   \______   \_____    ______ ______
 /  /_\  \|  | |  |/ __ \ /    \   |     ___/\__  \  /  ___//  ___/
/    |    \  |_|  \  ___/|   |  \  |    |     / __ \_\___ \ \___ \ 
\____|__  /____/__|\___  >___|  /  |____|    (____  /____  >____  >
        \/             \/     \/                  \/     \/     \/ 
                        A L I E N P A S S

         Secure Password Generator - code by Md. Al-Amin
         
=====================================================================
"""
print(banner)

print(" Welcome to the Alien Pass Password Generator!\n")

# input
while True:
    try:
        length = int(input("[+] Enter the desired password length (8–20): "))
        if 8 <= length <= 20:
            break
        else:
            print(" ! Please enter a number between 8 and 20.")
    except ValueError:
        print(" ! Please enter a valid number.")

while True:
    response = input("[+] Include uppercase letters (A–Z)? [y/n]: ").strip().lower()
    if response in ['y', 'n']:
        use_upper = (response == 'y')
        break
    print(" ! Invalid input. Please enter 'y' or 'n'.")

while True:
    response = input("[+] Include symbols (!@#$%^&* etc)? [y/n]: ").strip().lower()
    if response in ['y', 'n']:
        use_symbols = (response == 'y')
        break
    print(" ! Invalid input. Please enter 'y' or 'n'.")

while True:
    response = input("[+] Avoid confusing characters (I, l, B, 8, 5, S)? [y/n]: ").strip().lower()
    if response in ['y', 'n']:
        avoid_confusing = (response == 'y')
        break
    print(" ! Invalid input. Please enter 'y' or 'n'.")

while True:
    try:
        num_passwords = int(input("[+] How many passwords would you like to generate?: "))
        if num_passwords > 0:
            break
        else:
            print("! Enter a positive integer.")
    except ValueError:
        print(" ! Please enter a valid number.")

# Character sets 
lower = string.ascii_lowercase
numbers = string.digits
upper = string.ascii_uppercase if use_upper else ""
symbols = "!@#$%^&*()-_=+?" if use_symbols else ""

# character pool
char_pool = lower + numbers + upper + symbols

if avoid_confusing:
    for ch in "O0Il1IO0S5B8":
        char_pool = char_pool.replace(ch, "")

# Generate passwords
print("\n----------------------------------------")
print("  Generating your secure password(s)...\n")

passwords = []
for i in range(num_passwords):
    if not char_pool:
        print("\n ! Error: Character pool is empty. Check your options.")
        break
        
    password = ''.join(random.choice(char_pool) for _ in range(length))
    passwords.append(password)
    print(f"{i+1}. {password}")

# Create folder and save passwords
folder_name = "AlienPass_Generated_Passwords"
try:
    os.makedirs(folder_name, exist_ok=True)
except OSError as e:
    print(f" ! Could not create folder '{folder_name}': {e}")
    
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"passwords_{timestamp}.txt"
file_path = os.path.join(folder_name, file_name)

try:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(banner)
        file.write("🔐 Generated Passwords\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Password Length: {length}\n\n")
        for i, pw in enumerate(passwords, start=1):
            file.write(f"{i}. {pw}\n")
    print("\n All generated passwords have been saved successfully!")
    print(f" File location: {os.path.abspath(file_path)}")

except Exception as e:
    print(f" ! Failed to write file: {e}")

print("\n Done! Keep your passwords safe and private.")
