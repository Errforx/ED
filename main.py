import time
import os
import base64
import pyperclip

def clear():
    if os.name == 'nt':
        os.system('cls') # For windows Users
    else:
        os.system('clear') # For Linux/Mac Users

clear()

def E():
    msg = input(':: ').encode('utf-8')
    a = base64.b64encode(msg)
    f = a.decode('utf-8')
    print(f)

def D():
    msg = input(':: ').encode('utf-8')
    b = base64.decodebytes(msg)
    print(b.decode())

print(time.ctime())

choices = """\n\n Encryptor/Decryptor
                ---------------------------
                    Errforx@Wh4t3v3r
                        v.0.1
                
                1. Encrypt a Message
                2. Decrypt a Message

                3. Cancel"""
print(choices)
e = input('<:> ')

if e == '1':
    E()
elif e == '2':
    D()
elif e == '3':
    exit()
else:
    print('Invalid Input, Try again :(')
