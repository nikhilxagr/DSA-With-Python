# ============================================================
#               PYTHON FOR CYBERSECURITY
# ============================================================

# Python is one of the MOST used languages in cybersecurity
# because it is:
# - Simple & powerful
# - Excellent for automation
# - Rich in security-related libraries
# - Widely used in ethical hacking tools

# ============================================================
#           WHY PYTHON IN CYBERSECURITY?
# ============================================================

# 1. Automates repetitive security tasks
# 2. Used in penetration testing
# 3. Helps in log analysis & forensics
# 4. Used for malware analysis (basics)
# 5. Helps build custom security tools

# ============================================================
#           PYTHON + CYBERSECURITY USE CASES
# ============================================================

# +----------------------+------------------------------------+
# | Area                 | Usage                              |
# +----------------------+------------------------------------+
# | Automation           | Scanning, brute-force scripts      |
# | Networking           | Port scanning, packet analysis     |
# | Web Security         | Web scraping, vulnerability tests |
# | Cryptography         | Hashing, encryption                |
# | Forensics            | Log analysis                       |
# | Malware Analysis     | Static analysis                    |
# +----------------------+------------------------------------+

# ============================================================
#           1. AUTOMATION SCRIPT (BASIC)
# ============================================================

# Example: Renaming files (useful in log handling)

import os

def rename_files(path):
    for file in os.listdir(path):
        if file.endswith(".txt"):
            new_name = "log_" + file
            os.rename(os.path.join(path, file),
                      os.path.join(path, new_name))

# rename_files("logs")

# ============================================================
#           2. PORT SCANNER (BASIC)
# ============================================================

import socket

def port_scanner(target, ports):
    print(f"Scanning target: {target}")

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

# Example usage (localhost only for practice)
# port_scanner("127.0.0.1", range(20, 100))

# ============================================================
#           3. PASSWORD STRENGTH CHECKER
# ============================================================

import re

def password_strength(password):
    if len(password) < 8:
        return "Weak"

    if not re.search("[a-z]", password):
        return "Weak"
    if not re.search("[A-Z]", password):
        return "Weak"
    if not re.search("[0-9]", password):
        return "Weak"
    if not re.search("[@#$%&]", password):
        return "Weak"

    return "Strong"

print(password_strength("Python@123"))

# ============================================================
#           4. HASHING PASSWORDS (CRYPTOGRAPHY)
# ============================================================

import hashlib

def hash_password(password):
    hashed = hashlib.sha256(password.encode())
    return hashed.hexdigest()

print("Hashed password:", hash_password("admin123"))

# ============================================================
#           5. FILE INTEGRITY CHECKER
# ============================================================

# Used to detect file tampering

def file_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

# print(file_hash("important.txt"))

# ============================================================
#           6. SIMPLE BRUTE FORCE (EDUCATIONAL)
# ============================================================

# ⚠️ FOR EDUCATIONAL PURPOSE ONLY
# NEVER attack real systems without permission

def brute_force(password):
    wordlist = ["1234", "password", "admin", "admin123", "Python@123"]

    for word in wordlist:
        if word == password:
            print("Password cracked:", word)
            return
    print("Password not found")

# brute_force("admin123")

# ============================================================
#           7. LOG FILE ANALYSIS
# ============================================================

def analyze_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line or "FAILED" in line:
                print("Suspicious log:", line.strip())

# analyze_logs("server.log")

# ============================================================
#           8. EMAIL VALIDATION (PHISHING CHECK)
# ============================================================

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

print(validate_email("user@gmail.com"))
print(validate_email("user@fake"))

# ============================================================
#           9. SIMPLE KEYLOGGER (CONCEPT ONLY)
# ============================================================

# ⚠️ DO NOT IMPLEMENT MALICIOUS CODE
# This is ONLY to understand how attackers think

# Real ethical hackers study this to PREVENT attacks

# Example concept:
# - Capture keystrokes
# - Store them securely
# - Detect suspicious behavior

# ============================================================
#           10. CYBERSECURITY AUTOMATION IDEA
# ============================================================

# - Auto scan open ports
# - Auto check weak passwords
# - Auto monitor logs
# - Auto send alert email

# ============================================================
#           IMPORTANT ETHICAL WARNING
# ============================================================

# ⚠️ WARNING:
# Use Python for cybersecurity ONLY on:
# - Your own systems
# - Lab environments (TryHackMe, Hack The Box)
# - Authorized penetration tests

# Unauthorized access is ILLEGAL.

# ============================================================
#           IMPORTANT POINTS
# ============================================================

# 1. Python is a CORE skill for ethical hackers
# 2. Automation separates beginners from pros
# 3. Always learn networking with Python
# 4. Combine Python with Linux & Bash
# 5. Ethics matter more than skills

# ============================================================
#           NEXT STEPS (VERY IMPORTANT)
# ============================================================

# 1. Learn Python + Networking deeply
# 2. Practice on TryHackMe & Hack The Box
# 3. Build custom tools
# 4. Read real exploit scripts (educational)
# 5. Move to Advanced Security Libraries

# ============================================================
# End of File: 026 Python_For_Cybersecurity.py
# ============================================================
