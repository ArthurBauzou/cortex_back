from pymongo import MongoClient
import os, json, urllib.parse
from dotenv import load_dotenv
from pprint import pprint

# chargement du login/mdp
load_dotenv()
db_password = os.getenv("DB_ROOT_PASSWORD")
db_username = os.getenv("DB_ROOT_USERNAME")
password = urllib.parse.quote_plus(db_password)
username = urllib.parse.quote_plus(db_username)

#connexion à la base de données
client = MongoClient(f"mongodb://{username}:{password}@127.0.0.1:27017/")
db = client.cortex

#–––––––––––––#
## FONCTIONS ##
#–––––––––––––#

def testinsert():

    with open("../blankman.json", 'r', encoding='utf-8') as jsonfile:
        blankman = json.load(jsonfile)

    db.personnage.drop()
    db.personnage.insert_one(blankman)

def testread():
    data = db.personnage.find_one({}, {'_id': 0})
    return data

# pprint(testread())