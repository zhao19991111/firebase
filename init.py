from db import firebaseAPI
from config import firebaseConfig

def authenticate(firebase):
    email = input("Email: ")
    passwd = input("Password: ")
    info = {
        "email": email,
        "passwd": passwd
    }
    firebase.auth(info) # authenticate the user

def main():
    firebase = firebaseAPI(firebaseConfig)
    authenticate(firebase)    

if __name__ == "__main__":
    main()