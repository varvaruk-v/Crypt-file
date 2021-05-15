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
    delete = str(input("Do you want to delete original file? (Y/N) "))
    if delete.lower() == "y" or delete.lower() == "yes":
        os.remove(file)
        print("[INFO]: Original file was deleted")

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
        delete = str(input("Do you want to delete encrypted file? (Y/N) "))
        if delete.lower() == "y" or delete.lower() == "yes":
            os.remove(file)
            print("[INFO]: Encrypted file was deleted")
    except:
        print("[Error]: Wrong password or file is damaged!")

os.system('cls||clear')
print("""
                                                                                                    
                                                                                                    
     `./osyyso+:.                                                :ooooooooo   ``   /o/        v.1.2.1     
   `odMNdyssyhmNN-                                               sMMyyyyyyy  +mh   hMy              
  :mMm/`       .:.                                       ./      sMM`        .+:   hMy              
 -NMh`              /+- -oo/``/+-     :+/ .+++++/-`    .sNm+++-  sMM`        -+/   hMy    `:+oo+-   
 yMM`               dMyyhydN/ +MN-   :MM/ /MMhhhdNNy. -ymMNyyy:  sMMddddddd` oMd   hMy   /mNhoohMh. 
 yMM`               dMm.   `   +MN- -NMo  /MM`   `sMN`  yMh      sMM+//////  oMd   hMy  :MN-    oMd 
 :MMs               dMs         oMN:NMs   /MM`     MM+  yMh      sMM`        oMd   hMy  sMNhhhhhhhh`
  /NMh:         --  dMo          oMMMy    /MM`    /MM-  yMh      sMM`        oMd   hMy  /MM-      ` 
   .yNMNhsoooydNM+  dMo          `NMy     /MMo//+yMN/   /MNo/+y  sMM`        oMd   hMy   +NMho++shm 
     `:osyhhyyo/.   os/         `dMh`     /MMsyhys/`     :shhy+  /ss         :so   +s/    `+yhhys+. 
                                hMd`      /MM`                                                      
                               yMm.       /MM`                                                      
                              :yy.        -yy`                                                      
                                                                                                    
                                                                                                    
""")

mode = input("[+] Do you want encrypt or decrypt file? (E/D) ").lower()
dir = input("[+] Enter file: ")
print("--------------------")
password = input("[+]Enter password: ")

if mode == "e" or mode == "en" or mode == "encrypt":
    encrypt(dir, password)
elif mode == "d" or mode == "de" or mode == "decrypt":
    decrypt(dir, password)