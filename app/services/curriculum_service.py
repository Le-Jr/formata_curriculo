from flask_pymongo import PyMongo
from uuid import uuid4

mongo = None

def init_mongo(app):
    global mongo
    mongo = PyMongo(app)


def create_curriculum(name, email, celphone, experience, resume):
    curriculum = {
        "id": str(uuid4()),
        "name": name,
        "email": email,
        "celphone": celphone,
        "expericence": experience,
        "resume": resume,
    }

    mongo.db.curriculos.insert_one(curriculum)
    return curriculum