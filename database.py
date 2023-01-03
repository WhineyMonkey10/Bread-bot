from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Da code
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['bread']
collection = db['currency']

class Database:

    def get_currency(user_id):
        bal = collection.find_one({"user_id": user_id})
        if bal == None:
            return "User does not exist, please use the command `/start` to get started!"
        elif bal != None:
            return bal['currency']
    def update_currency(user_id, currency):
        if Database.checkifuser(user_id):
            collection.update_one({"user_id": user_id}, {"$set": {"currency": currency}})
            return "Currency updated!"
        elif Database.checkifuser(user_id) == False:
            return "User does not exist, please use the command `/start` to get started!"
    def add_currency(user_id, currency):
        if Database.checkifuser(user_id):
            collection.update_one({"user_id": user_id}, {"$inc": {"currency": currency}})
            return "Currency added!"
        elif Database.checkifuser(user_id) == False:
            return "User does not exist, please use the command `/start` to get started!"
        
    def remove_currency(user_id, currency):
        if Database.checkifuser(user_id):
            collection.update_one({"user_id": user_id}, {"$inc": {"currency": -currency}})
            return "Currency removed!"
        elif Database.checkifuser(user_id) == False:
            return "User does not exist, please use the command `/start` to get started!"
    def checkifuser(user_id):
        if collection.find_one({"user_id": user_id}) == None:
            return False
        else:
            return True
    def adduser(user_id):
        if Database.checkifuser(user_id):
            return "User already exists"
        elif Database.checkifuser(user_id) == False:
            collection.insert_one({"user_id": user_id, "currency": 10000})
            return True
    def start(user_id):
        if Database.adduser(user_id) == "User already exists":
            return "You already have an account!"
        elif Database.adduser(user_id):
            return "Welcome! Here are 10,000 bread bucks to get you started!"
    def get_leaderboard():
        # Get the User ID and Currency of all users and find the top 10 richest users
        top10 = list(collection.find({}, {"user_id": 1, "currency": 1}).sort("currency", -1).limit(10))
        top10 = [f"{user['user_id']}: {user['currency']}" for user in top10]
        return ''.join(top10)
    def getotherscurrency(user_id):
        user = collection.find_one({"user_id": user_id})
        if user == None:
            return "User does not exist!"
        elif user != None:
            return f"{user['user_id']}: {user['currency']}"
    def rob(user_id, target_id, amount):
        import random
        chance = random.randint(1, 100)
        if chance <= 25:
            Database.remove_currency(user_id, amount)
            Database.add_currency(target_id, amount)
            return f"You tried to rob {target_id} but failed and lost {amount} bread bucks!"
        elif chance > 25:
            Database.add_currency(user_id, amount)
            Database.remove_currency(target_id, amount)
            return f"You successfully robbed {target_id} and got {amount} bread bucks!"