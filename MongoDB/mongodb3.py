import pymongo
url="mongodb://localhost:27017/"
c=pymongo.MongoClient(url)
db=c["sample"]
coll=db["Student"]
coll.insert_many([{"rollno":2,"name":"athaman"},{"rollno":3,"name":"gokul"}])
print(c.database_names())
