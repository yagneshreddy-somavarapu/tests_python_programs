import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB using the connection string
dem = MongoClient("mongodb+srv://prostack:24-june-2003@codingeditor.g4mgtzy.mongodb.net/?retryWrites=true&w=majority&appName=codingEditor")

# Access the database and collection
dem_db = dem['codingEditor']
dem_col = dem_db['Emails']

# Fetch all documents from the collection
db = dem_col.find({}, {})

# Convert cursor to a list
res = []
for i in db:
    res.append(i)

# Print the result
print(res)
