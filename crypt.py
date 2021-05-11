import pyAesCrypt
import os
def encrypt(file, password):
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(
        str(file),
        str(file)+".aes",
        password,
        bufferSize
    )
    # os.remove(file)
    print(f"[SUCCESS]: File {file} successfully encrypted")
    delete = str(input("Do you want to delete original file? (Y/N)"))
    if delete.lower() == "y" or delete.lower() == "yes":
        os.remove(file)
        print("Original file was deleted")
def decrypt(file, password):
    bufferSize = 512*1024
    try:
        pyAesCrypt.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]),
            password,
            bufferSize
        )
        print(f"[SUCCESS]: File {file} successfully decrypted")
    except:
        print("[Error]: Wrong password!")

dir = input("Enter file: ")
print("--------------------")
password = input("Enter password: ")

if ".aes" in dir:
    decrypt(dir, password)
else:
    encrypt(dir, password)