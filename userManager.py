from fileLoader import *
from indexer import *
from models import User
import pickle

userNames = set()
users = dict()

def createUsers():
    
    if tryFile("Data/users.pkl"):
        with open(f"Data/users.pkl", "rb") as file:
            users = pickle.load(file)
            
    else:
        
        users = {
            "admin": User("admin")
        }
    
        with open(f"Data/users.pkl", "wb") as file:
            pickle.dump(users, file)
            
    for user in users:
        
        userNames.add(user)
        
        users[user].notes, users[user].words = index(users[user])
            
    return users, userNames