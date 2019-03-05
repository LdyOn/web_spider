from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.blog_database
collection = db.blog
collection.insert_one({'id':123,'name':'xiaoming'})