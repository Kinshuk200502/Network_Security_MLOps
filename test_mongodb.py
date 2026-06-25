from pymongo.mongo_client import MongoClient

uri="mongodb+srv://kinshukmishra2005_db_user:Kinshuk02@cluster0.0prgym7.mongodb.net/?appName=Cluster0"

client=MongoClient(uri)

try: 
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)