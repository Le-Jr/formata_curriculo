from app import mongo
from uuid import uuid4

def create_curriculum(name, email):
    curriculum = {
        "id": str(uuid4()),
        "name": name,
        "email": email,
    }

    mongo.db.insert_one(curriculum)
    return curriculum