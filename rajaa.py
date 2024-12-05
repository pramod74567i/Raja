#father of developer tg @KIING_OP
from cryptography.fernet import Fernet

#anti decrypted this project
with open('enc', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)


with open('raja.py', 'rb') as encrypted_file:
    encrypted_code = encrypted_file.read()


decrypted_code = cipher.decrypt(encrypted_code)


exec(decrypted_code)