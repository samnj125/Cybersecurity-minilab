# Fernet is a python tool to encrypt/decrypt safely
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)  # creates a secret key

encrypted = cipher.encrypt(b"My Secret Message")
decrypted = cipher.decrypt(encrypted)
