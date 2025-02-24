from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file :
        key_file.write(key)

def load_key() :
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter master password : ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def add():
    userName = input("Enter username : ")
    pwd = input("Enter password : ")
    with open("passwords.txt", 'a') as f:
        f.write(userName + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open("passwords.txt",'r') as f :
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("Username : ",user, ", Password : ", fer.decrypt(passw.encode()).decode())
      
        

while True :
    mode = input("Select mode. (add/view). Press q for quit : ").lower()

    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid choice")
    
