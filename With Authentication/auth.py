import os
import sys
import hashlib
import sqlite3
from home import main as MainMenu
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from typing import Optional

class AuthenticationManager:
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.conn: Optional[sqlite3.Connection] = None
        self.connect_to_db()

    def connect_to_db(self) -> None:
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.create_table()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            exit(1)

    def create_table(self) -> None:
        try:
            if self.conn is not None:
                cursor = self.conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS users
                                  (email TEXT PRIMARY KEY, password TEXT)''')
                self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            if self.conn is not None:
                self.conn.rollback()

    def register_user(self, email: str, password: str) -> None:
        try:
            password_hash = self._hash_password(password)
            if self.conn is not None:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password_hash))
                self.conn.commit()
                print("User registration successful")
        except sqlite3.IntegrityError:
            print("User already exists")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def _hash_password(self, password: str) -> bytes:
        salt = os.urandom(32)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        return salt + key

    def verify_password(self, email: str, password: str) -> bool:
        try:
            if self.conn is not None:
                cursor = self.conn.cursor()
                cursor.execute("SELECT password FROM users WHERE email=?", (email,))
                row = cursor.fetchone()
                if row:
                    user_password_hash = row[0]
                    salt = user_password_hash[:32]
                    key = user_password_hash[32:]
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend()
                    )
                    new_key = kdf.derive(password.encode())
                    return new_key == key
                else:
                    return False
            else:
                return False  # Handle case where self.conn is None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False  # Handle exception case
        
def start():
    db_file = "./auth.db"
    auth_manager = AuthenticationManager(db_file)
    auth_manager.register_user("user@example.com", "password123")

    print("----- Welcome to Insophinia Vehicle Management System -----\n")
    
    while True:
        try:
            print("Authentication Portal")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if auth_manager.verify_password(email, password):
                print("Login successful")
                MainMenu()
            else:
                print("Incorrect password or user does not exist")
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    start()
    sys.exit(0)
