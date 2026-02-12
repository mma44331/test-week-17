import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


mongo_uri = os.getenv("MONGO_URI","mongodb://mongodb:27017/")
mongo_db = os.getenv("MONGO_DB","mymongodb")
mongo_coll = os.getenv("MONGO_COLLECTION","ordersandcustomers")

def get_con_db():
    client = pymongo.MongoClient(mongo_uri)
    db = client[mongo_db]
    return db[mongo_coll]

