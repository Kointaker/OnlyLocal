# OnlyLocal App

# Imports
import sqlite3
from cryptography.fernet import Fernet
import time

key1 = Fernet.generate_key()
key1 = Fernet.generate_key()
key1 = Fernet.generate_key()
key1 = Fernet.generate_key()
f = Fernet(key1)
token = f.encrypt(b"my deep dark secret")
print(token)
print(f.decrypt(token))
print(f)





def main():
    pass













if __name__ == "__main__":
    main()