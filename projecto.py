from cryptography.fernet import Fernet
import pyotp
import hashlib



with open("otp_secret.txt", "r") as f:
    secret = f.read()

totp = pyotp.TOTP(secret)







master_pwd = input("Enter master password: ")
hashed = hashlib.sha256(master_pwd.encode()).hexdigest()

with open("master.txt", "r") as f:
    stored = f.read()

if hashed != stored:
    print("Wrong password! Access denied.")
    exit()

otp = input("Enter OTP: ")

if not totp.verify(otp):
    print("Invalid OTP! Access denied.")
    exit()

def load_key():
    file = open("key.key","rb") 
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


'''
def write_key():
    key = Fernet.generate_key()
    
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''





def readfile():

    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:",fer.decrypt(passw.encode()).decode())


def writefile():

    name = input("Username: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 


'''
import hashlib

master_pwd = input("Set your master password: ")
hashed = hashlib.sha256(master_pwd.encode()).hexdigest()

with open("master.txt", "w") as f:
    f.write(hashed)

print("Master password set!")
'''



while True:
    print("1. Read file")
    print("2. Write file")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        readfile()

    elif choice == "2":
        
        writefile()
    elif choice == "3":
        
        break
    
    else:
        print("Invalid choice. Please try again.")

