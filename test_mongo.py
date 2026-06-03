from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["pad_vending_machine"]

products = db["products"]

products.insert_one({
    "name": "Whisper Large",
    "price": 10,
    "stock": 50
})

print("Inserted Successfully")