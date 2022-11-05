from cryptography.fernet import Fernet

pwd = input("Enter your master password: ")


def load_key():
    file = open("E_D_key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key() + pwd.encode()
fer = Fernet(key)

'''
def generate_key():
    key = Fernet.generate_key()
    with open("E_D_key.key","wb") as key_file:
        key_file.write(key)
'''



def add():
    account_name = input("Enter account name:")
    password = input("Enter the password for the account:")

    with open('passwords.txt','a') as f:
        f.write(account_name + "|" + str(fer.encrypt(password.encode()).decode()) + "\n")


def view():
    with open('passwords.txt') as f:
        for line in f.readlines():
            data = line.rstrip()
            username, passw = data.split('|')
            print("Username: ",username, "Password: ",fer.decrypt(passw.encode()))
            
            

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add) or press q to quit: ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add() 
    else: 
        print("Invalid mode.")
        continue

