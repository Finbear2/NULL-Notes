from fileLoader import *
from indexer import *
from models import User
import string
import pickle

userNames = None
users = None

def createUsers():
    
    global userNames, users
    
    userNames = set()
    users = dict()
    
    if tryFile("Data/users.pkl"):
        with open(f"Data/users.pkl", "rb") as file:
            users = pickle.load(file)
            
    else:
        
        users = {
            "default": User("default")
        }
    
        with open(f"Data/users.pkl", "wb") as file:
            pickle.dump(users, file)
            
    for user in users:
        
        userNames.add(user)
        
        users[user].notes, users[user].words = index(users[user])
            
    return users, userNames

def getUser(name):
    
    if userNames:
        if isinstance(name, str):
            return users[name]
        else:
            return name
    else:
        return None