import pymongo
url="mongodb://localhost:27017/"
c=pymongo.MongoClient(url)
print(c.database_names())
