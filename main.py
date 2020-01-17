import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()

# print(client)

db = client['test-database']

# print(db)

courses = db.courses
courses1 = db.courses1

# print(courses)
# course = {
#     'author': 'A1',
#     'course': 'C1',
#     'price' : 100,
#     'rating': 5
# }
#
# arr_courses = [
#     {
#         'author': 'A2',
#         'course': 'C2',
#         'price' : 99,
#         'rating': 4
#     },
#     {
#         'author': 'A3',
#         'course': 'C3',
#         'price' : 98,
#         'rating': 3
#     },
#     {
#         'author': 'A4',
#         'course': 'C4',
#         'price' : 97,
#         'rating': 2
#     }
# ]

# res = courses.insert_one(course)
# print(res)
#
# res2 = courses.insert_many(arr_courses)
# print(res2)

# for object_id in res2.inserted_ids:
#     print('Course Added. The course id is ', object_id)
#
# if res.acknowledged:
#     print('Course Added. The course id is ', res.inserted_id)

# courses.update({
#     'price': 99
# }, {
#     '$set': {
#         'price': 100
#     }
# }, multi=True
# )

# courses.delete_one({
#     'author': 'Rishi'
# })

# print(list(courses.aggregate(
#     [
#         {
#             "$group": {
#                 '_id': '$author',
#                 'ranking': {
#                     '$avg': '$rating'
#                 }
#             }
#         }
#     ]
# )))

courses1.create_index(
    [('course', 1)],
    unique=True
)

courses = courses.find().sort([('price', 1), ('rating', -1)]).limit(2)

for course in courses:
    pprint.pprint(course)

