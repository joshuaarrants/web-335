from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335

db.users.update_one(

    {"employee_id": "0000010"},

    {

        "$set": {

            "email": "jwarrants@my365.bellevue.edu"

        }

    }

)

pprint.pprint(db.users.find_one({"employee_id": "0000010"}, {"email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))