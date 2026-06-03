from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["pad_vending_machine"]

products = db["products"]

print("Connected Successfully")