

from pymongo import MongoClient as MC

client = MC("localhost", 27017)

COLLEGE_DB = client.college
COLLECTION = COLLEGE_DB.students

print("Female students of MCA Department: ")
query = COLLECTION.find({"gender":"female"})
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])


print("\nStudent with highest mark in MCA department: ")
query = COLLECTION.find({}).sort("mark", -1)
print(query[0])

print("\nMale students who secured A+: ")
query = COLLECTION.find({"grade":"A+", "gender":"male"})
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])

print("\nNames of Top 3 Mechanical Students: ")
query = COLLECTION.find({"course": "Mechanical"}).sort("mark", -1).limit(3)
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])

print("\nNames of Female students who scored more than 98: ")
query = COLLECTION.find({"mark":{"$gt": 98}, "gender":"female"})
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])

print("\nNames of students who scored more than 80 but less than 90: ")
query = COLLECTION.find({"mark":{"$gt": 80, "$lt":90}})
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])

print("\Details of students whose name starts with 'B': ")
query = COLLECTION.find({"name.fname": {"$regex": "^(B)"}})
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])    

print("\nNames of students who are from Kollam: ")
query = COLLECTION.find({"address.city":"Kollam"})
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])

print("\nNames of students who are from neither Kollam nor Trivandrum: ")
query = COLLECTION.find({"address.city":{"$ne": "Kollam", "$ne":"Trivandrum"}})
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])

print("\nNames of students who are from Kollam or Trivandrum: ")
query = COLLECTION.find({"address.city":{"$in": ["Kollam", "Trivandrum"]}})
for q in query:
    print(q["name"]["fname"] + q["name"]["lname"])
