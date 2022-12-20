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

    def get_balance(user_id, currency):
        currency = collection.find_one({'user_id': user_id, 'currency': currency})
        currency.pop('_id')
        currency.pop('user_id')
        if currency == None:
            return "You don't have any currency!"
        else:
            return currency
    
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
    def rob(user_id, amount):
        collection.find_one_and_update({'user_id': user_id}, {'$inc': {'currency': -amount}})
        return True
    def checkIfUserExists(user_id):
        if collection.find_one({'user_id':user_id}):
            return True
        else:
            return False

Database.add_user(123456789)