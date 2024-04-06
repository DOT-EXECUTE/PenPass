from cryptography.fernet import Fernet
from sys import platform
import os


if platform == "win32":
    HashesPath = r'c:\\Program Files\\PenPass\\Hashes'

    if not os.path.exists(HashesPath):
        os.chdir('c:\\Program Files')
        os.mkdir(HashesPath)
elif platform == "linux":
    HashesPath = '/usr/PenPass/Hashes'

    if not os.path.exists(HashesPath):
            os.makedirs(HashesPath)

KeyFilePath = os.path.join(HashesPath, 'EncryptionKey.key')

# Generate and store encryption key if it doesn't exist
if not os.path.exists(KeyFilePath):
    key = Fernet.generate_key()
    with open(KeyFilePath, 'wb') as KeyFile:
        KeyFile.write(key)


def LoadKey():
    with open(KeyFilePath, 'rb') as KeyFile:
        key = KeyFile.read()
    return key

# Function for encrypting passwords
def EncryptPassword(password):
    key = LoadKey()
    cipher_suite = Fernet(key)
    EncryptedPassword = cipher_suite.encrypt(password.encode())
    return EncryptedPassword

# Function for decrypting passwords
def DecryptPassword(EncryptedPassword):
    key = LoadKey()
    cipher_suite = Fernet(key)
    DecryptedPassword = cipher_suite.decrypt(EncryptedPassword).decode()
    return DecryptedPassword

