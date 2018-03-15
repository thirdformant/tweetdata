import os
import pymongo
from dotenv import find_dotenv, load_dotenv

def mongodb_connect():
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    client = pymongo.MongoClient(os.environ.get("DATABASE_URL"), 27017)
    db = client.tweetbase
    return db
