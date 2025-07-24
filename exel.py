import pandas as pd
from pymongo import MongoClient


file_path = 'Untitled form.csv'  
df = pd.read_csv(file_path)

df["marks"] = 0
df["Attempt"] = "Not Attempt"

json_data = df.to_dict(orient='records')

print(json_data)

client = MongoClient('mongodb://localhost:27017/') 
db = client['codingEditor'] 
collection = db['Emails'] 
Mongo_data = collection.find({},{'_id':0})
li = []
for data in Mongo_data:
    li.append(data["email"])
    print(data["email"])
insert_count = 0
duplicate_count = 0
for index,record in enumerate(json_data):
    if record["email"] not in li:
        print(record["email"],">>>✅ is present")
        collection.insert_one(record)
        insert_count += 1
    else:
        print(record["email"],">>>❌ is not present")
        duplicate_count += 1
print(f"Total inserted count is {insert_count}\nTotal Duplicates Count is {duplicate_count}")


