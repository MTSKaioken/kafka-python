import os

from pymongo import MongoClient

def get_connection():
    CONNECTION_STRING = os.getenv('STRING_CONNECTION_MONGODB')
    client = MongoClient(CONNECTION_STRING)
    try:
        db_name = client['estoque']
        return db_name
        # customers = dbname['customers']
        # resp = customers.find()
    except Exception as e:
        print(e)