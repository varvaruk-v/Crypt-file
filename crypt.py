import pyAesCrypt
import os

def encrypt(data, key, method):
    import requests as r
    enc = r.get(f"https://api.vaar.pp.ua/crypt/?data={data}&key={key}&method={method}&mode=e")
    status_code = enc.status_code
    enc = enc.json()
    if status_code == 200:
        return enc["text"]
    else:
        return "[Error] "+str(enc["message"])

def decrypt(data, key, method):
    import requests as r
    enc = r.get(f"https://api.vaar.pp.ua/crypt/?data={data}&key={key}&method={method}&mode=d")
    status_code = enc.status_code
    enc = enc.json()
    if status_code == 200:
        return enc["text"]
    else:
        return "[Error] "+str(enc["message"])
def EncryptFile(file, password):
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(
        str(file),
        str(file)+".aes",
        password,
        bufferSize
    )
    # os.remove(file)
    print(f"[SUCCESS]: File {file} successfully encrypted")
    delete = str(input("Do you want to delete original file? (Y/N) "))
    if delete.lower() == "y" or delete.lower() == "yes":
        os.remove(file)
        print("[INFO]: Original file was deleted")

def DecryptFile(file, password):
    bufferSize = 512*1024
    try:
        pyAesCrypt.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]),
            password,
            bufferSize
        )
        print(f"[SUCCESS]: File {file} successfully decrypted")
        delete = str(input("Do you want to delete encrypted file? (Y/N) "))
        if delete.lower() == "y" or delete.lower() == "yes":
            os.remove(file)
            print("[INFO]: Encrypted file was deleted")
    except:
        print("[Error]: Wrong password or file is damaged!")

os.system('cls||clear')
print("""                                                                    
                                                                                                    
                                                                                                    
       ```````                                                    ```                         v.1.2.2      
    .ohdmNNNmdy/`                                                sddd`                              
  `sMMMMMNNNMMMMm:   ```  ````  ````     `````  ```   ````     `-MMMM.``     ```````      ````  ``` 
  sMMMMm:``.+MMMMN. -mmmh/dMMd -mmmmy   `dmmmo ommmoodNMMNh:  /mNMMMMmmy   :ydNMMMNdy:   `mmmd/dNMN 
  NMMMM/     +ssss. -MMMMMMMMm  oMMMM:  +MMMm` sMMMMMdhmMMMM+ :hNMMMMhhs `hMMMNysyNMMMh` `MMMMMMMMN 
 `MMMMM:            -MMMMN/..`   hMMMm `NMMM-  sMMMM/   dMMMN   yMMMM`   +MMMM:   :MMMM+ `MMMMN+..` 
  mMMMMs     sNNNN- -MMMMs       `mMMM+oMMMo   sMMMM.   hMMMM   yMMMM`   sMMMM.   .MMMMs `MMMMy     
  :MMMMMh+/+hMMMMd  -MMMMo        -NMMNNMMh    sMMMMh--/NMMMd   yMMMM:`  :MMMMs.`.sMMMM- `MMMMy     
   -hMMMMMMMMMMNs`  -MMMMo         /MMMMMN.    sMMMMMMMMMMMm.   +MMMMMMh  :mMMMMMMMMMd:  `MMMMy     
     `:osyyss+:`    `oooo:          dMMMM/     sMMMM:/syso:`     -osyys/    -+ssyss+-    `oooo:     
                                /yydMMMN+      sMMMM-                                               
                                omNNNds.       +dddd.                                               
                                 `````          ````                                                
                                                                                                    
""")
try:
    FileOrText = input("[+] What do yo want to crypt? (Text/File) ").lower()
    if FileOrText == "text" or FileOrText == "t":
        mode = input("[+] Do you want encrypt or decrypt text? (E/D) ").lower()
        data = input("[+] Enter text: ")
        print("--------------------")
        password = input("[+] Enter password: ")
        if mode == "e" or mode == "en" or mode == "encrypt":
            encrypted = encrypt(data, password, "AES-256-CBC")
            if "[Error]" in encrypted:
                print(encrypted)
            else:
                print("Encrypted text: "+str(encrypted))
        elif mode == "d" or mode == "de" or mode == "decrypt":
            decrypted = decrypt(data, password, "AES-256-CBC")
            if "[Error]" in decrypted:
                print(decrypted)
            else:
                print("Decrypted text: "+str(decrypted))
        else:
            print("[Error] Unknown mode")
    elif FileOrText == "file" or FileOrText == "f":
        mode = input("[+] Do you want encrypt or decrypt file? (E/D) ").lower()
        dir = input("[+] Enter file: ")
        print("--------------------")
        password = input("[+] Enter password: ")

        if mode == "e" or mode == "en" or mode == "encrypt":
            EncryptFile(dir, password)
        elif mode == "d" or mode == "de" or mode == "decrypt":
            DecryptFile(dir, password)
        else:
            print("[Error] Unknown mode")
    else:
        print("[Error] Unknown mode")
except:
    pass