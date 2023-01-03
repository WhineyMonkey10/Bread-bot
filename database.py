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
        # Make the user ID a mention and add the currency to the end and make a new line for each user
        for i in range(len(top10)):
            top10[i] = f"<@{top10[i]['user_id']}>: {top10[i]['currency']}" + " bread bucks" + ".\n"
        return ''.join(top10)
    def rob(user_id, target_id, amount):
        if Database.checkifuser(user_id) == False:
            return "You do not have an account! Please use the command `/start` to get started!"
        elif Database.checkifuser(user_id):
            if Database.checkifuser(target_id) == False:
                return "The target user does not have an account!"
            elif Database.checkifuser(target_id):
                # Check if the user has enough bread bucks
                if Database.get_currency(user_id) < amount:
                    return "You do not have enough bread bucks!"
                # Check if the target user has enough bread bucks
                if Database.get_currency(target_id) < amount:
                    return "The target user does not have enough bread bucks!"
                elif Database.get_currency(user_id) >= amount:
                    import random
                    chance = random.randint(1, 100)
                    if chance <= 25:
                        #amountlost = 75 / 100 * amount
                        #Database.remove_currency(user_id, amountlost)
                        #target_id = f"<@{target_id}>"
                        return f"You tried to rob {target_id} but failed!"
                    elif chance > 25:
                        Database.add_currency(user_id, amount)
                        Database.remove_currency(target_id, amount)
                        target_id = f"<@{target_id}>"
                        return f"You successfully robbed {target_id} and got {amount} bread bucks!"
    def pay(user_id, target_id, amount):
        if Database.checkifuser(user_id) == False:
            return "You do not have an account! Please use the command `/start` to get started!"
        elif Database.checkifuser(user_id):
            # Check if the target user exists
            if Database.checkifuser(target_id) == False:
                return "The target user does not have an account!"
            elif Database.checkifuser(target_id):
                # Check if the user has enough bread bucks
                
                if Database.get_currency(user_id) < amount:
                    return "You do not have enough bread bucks!"
                elif Database.get_currency(user_id) >= amount:
                    Database.remove_currency(user_id, amount)
                    Database.add_currency(target_id, amount)
                    str(target_id)
                    target_id = f"<@{target_id}>"
                    return f"You paid {target_id} {amount} bread bucks!"
    #def work(user_id):
    #    if Database.checkifuser(user_id) == False:
    #        return "You do not have an account! Please use the command `/start` to get started!"
    #    elif Database.checkifuser(user_id):
    #        # Check if the user is on cooldown, if they are, return a message saying they are on cooldown, if they are not, let them work. Check if they are on cooldown by checking the lastest instance of their user ID in the work cooldown file and compare its time to the current time. If the time is less than 5 minutes, return a message saying they are on cooldown, if it is more than 5 minutes, let them work.
    #        f = open("workcooldowns.txt", "r")
    #        if f.read().find(user_id):
    #            if datetime.datetime.now() - datetime.timedelta(minutes=5) > datetime.datetime.now():
    #                return "You are on cooldown!"
    #            else:
    #                import random
    #                odds = random.randint(1, 100)
    #                if odds <= 25:
    #                    import datetime
    #                    # OPen the work cooldown file and add the user to it
    #                    f = open("workcooldowns.txt", "a")
    #                    f.write(f"{user_id}" + f" {datetime.datetime.now()}")                 
    #                    return "You worked but did not earn any bread bucks! You are now on a 5 minute cooldown!"
    #                elif odds > 25:
    #                    amount = random.randint(1, 1832)
    #                    oddsof5kplus = random.randint(1, 100)
    #                    if oddsof5kplus <= 10:
    #                        amount = random.randint(5000, 10000)
    #                        Database.add_currency(user_id, amount)
    #                        return f"You worked and earned {amount} bread bucks! You are now on a 5 minute cooldown!"
    #                    elif oddsof5kplus > 10:
    #                        Database.add_currency(user_id, amount)
    #                        return f"You worked and earned {amount} bread bucks! You are now on a 5 minute cooldown!"

    def work(user_id):
        if Database.checkifuser(user_id) == False:
            return "You do not have an account! Please use the command `/start` to get started!"
        elif Database.checkifuser(user_id):
            import random
            odds = random.randint(1, 100)
            if odds <= 25:
                return "You worked but did not earn any bread bucks!"
            elif odds > 25:
                amount = random.randint(1, 1832)
                oddsof5kplus = random.randint(1, 100)
                if oddsof5kplus <= 10:
                    amount = random.randint(5000, 10000)
                    Database.add_currency(user_id, amount)
                    return f"You worked and earned {amount} bread bucks!"
                elif oddsof5kplus > 10:
                    Database.add_currency(user_id, amount)
                    return f"You worked and earned {amount} bread bucks!"