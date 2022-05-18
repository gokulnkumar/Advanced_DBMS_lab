import pymongo
url="mongodb://localhost:27017/"
c=pymongo.MongoClient(url)
db=c["sample"]
coll=db["Student"]
coll.insert_one({"rollno":1,"name":"bharath"})
print(c.database_names())
