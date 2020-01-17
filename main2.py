from pymongo import MongoClient

client = MongoClient()

db = client['test-2']

temp = db.temp

store = [
    {'x': 1, 'tags': ['dog', 'cat']},
    {'x': 2, 'tags': ['cat']},
    {'x': 2, 'tags': ['mouse', 'cat', 'dog']}
]

result = temp.insert_many(store)
print(result)
