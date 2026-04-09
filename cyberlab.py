import hashlib
import socket
from cryptography.fernet import Fernet
import threading


# ================= HASH GENERATOR =================
def hash_generator():
    text = input("Enter text to hash: ")

    print("\nChoose hashing algorithm:")
    print("1. MD5")
    print("2. SHA256")

    choice = input("Choice: ")
    if choice == "1":
        result = hashlib.md5(text.encode()).hexdigest()
    elif choice == "2":
        result = hashlib.sha256(text.encode()).hexdigest()
    else:
        print("Invalid choice.")
        return

    print(f"\nGenerated Hash:\n{result}\n")


# ================= PASSWORD CHECKER =================
def password_checker():
    password = input("Enter password to check strength: ")

    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in "!@#$%^&*" for char in password):
        strength += 1

    if strength <= 1:
        print("Weak Password\n")
    elif strength == 2:
        print("Moderate Password\n")
    else:
        print("Strong Password\n")


# ================= ENCRYPTION TOOL =================
def encryption_tool():
    key = Fernet.generate_key()
    cipher = Fernet(key)

    message = input("Enter message to encrypt: ")
    encrypted = cipher.encrypt(message.encode())

    print("\nEncrypted message:", encrypted.decode())
    print("Save this key to decrypt:", key.decode(), "\n")


# ================= PORT SCANNER =================
def port_scanner():
    target = input("Enter target IP: ")
    open_ports = []

    print(f"\nScanning {target}...\n")

    def scan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        if s.connect_ex((target, port)) == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

        s.close()

    for port in range(1, 1025):
        thread = threading.Thread(target=scan, args=(port,))
        thread.start()

    import time
    time.sleep(5)

    # Create report
    from datetime import datetime

    with open("scan_report.txt", "w") as file:
        now = datetime.now()
        file.write(f"Target: {target}\n")
        file.write(f"Scan Date: {now}\n\n")
        file.write("Open Ports:\n")

        for port in open_ports:
            file.write(f"- Port {port}\n")

    print("\nReport saved as scan_report.txt\n")


# ================= MAIN MENU =================
def main():
    while True:
        print("===== CYBERSECURITY MINI LAB =====")
        print("1. Hash Generator")
        print("2. Password Strength Checker")
        print("3. Encryption Tool")
        print("4. Port Scanner")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            hash_generator()
        elif choice == "2":
            password_checker()
        elif choice == "3":
            encryption_tool()
        elif choice == "4":
            port_scanner()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
