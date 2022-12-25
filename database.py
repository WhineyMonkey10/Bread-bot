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
    def __init__(self):
        self.db = db
        self.collection = collection

    def get_balance(user_id):
        # Find the user in the database
        user = collection.find_one({'user_id': user_id})
        # Get only the currency value
        return user
    
    def update_currency(user_id, amount, type):
        if type == 'add':
            collection.update_one({'user_id': user_id}, {'$inc': {'currency': amount}})
            return True
        elif type == 'remove':
            collection.update_one({'user_id': user_id}, {'$inc': {'currency': -amount}})
            return True
        else:
            return False
    def add_user(user_id):
        collection.insert_one({'user_id:': user_id, 'currency': 10000})
        return True
    def add_currency(user_id, amount):
        collection.update_one({'user_id': user_id}, {'$inc': {'currency': amount}})
    def robuser(victimUser_id, amount, user_id):
        import random
        if random.randint(1, 2) == 1:
            collection.find_one_and_update({'user_id': victimUser_id}, {'$inc': {'currency': -amount}})
            collection.find_one_and_update({'user_id': user_id}, {'$inc': {'currency': amount}})
            return True
        else:
            return False
    def pay(user_id, amount, victimUser_id):
        collection.find_one_and_update({'user_id:': user_id}, {'$inc': {'currency': -amount}})
        collection.find_one_and_update({'user_id:': victimUser_id}, {'$inc': {'currency': amount}})
        return True
    

