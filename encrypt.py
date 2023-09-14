# Простенький скрипт для шифрования проекта
import sys
import os
import base64

ignore_list = [
    'encrypt.py',
    'manage.py',
    'loader.py']


def encrypt_dir(path: str):
    """Шифруем директорию"""
    for root, _, files in os.walk(path):
        for file in files:
            if file[-3:] != ".py" or file in ignore_list:
                continue
            file_path = os.path.join(root, file)
            print(file_path + " is encrypting.")
            encrypt_file(file_path)
            os.remove(file_path)


def encrypt_file(path):
    """Шифруем файлы"""
    with open(path) as f:
        plain_text = f.read()
    base64_bytes = base64.b64encode(plain_text.encode('utf-8'))
    with open(path + "enc", "wb") as file_out:
        file_out.write(base64_bytes)


path = sys.argv[1]
if os.path.isdir(path) and os.path.exists(path):
    encrypt_dir(path)
elif os.path.isfile(path) and os.path.exists(path):
    encrypt_file(path)
