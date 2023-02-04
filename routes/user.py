from fastapi import APIRouter
from pydantic import BaseModel
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId 


user = APIRouter()

@user.get('/')
async def find_all_user():
    #print(conn.project.user.find())  address of the object
    #print(usersEntity(conn.project.user.find()))   actual data
    try:
        response_data = usersEntity(conn.project.user.find())
        response = {
            "Status": "Successful",
            "Payload": response_data
        }
        return response
    except Exception as e:
        return {
            "Status": "Error",
            "Info": str(e)
        }


@user.get('/{id}')
async def find_one_user(id):
    try:
        response_data = userEntity(conn.project.user.find_one({'_id': id}))
        response = {
            "Status": "Successful",
            "Payload": response_data
        }
        return response
    except Exception as e:
        return {
            "Status": "Error",
            "Info": str(e)
        }

class create_user_payload(BaseModel):
    firebase_id: str
    nick_name: str
    email: str

@user.post('/')
async def create_user(create_data_payload: create_user_payload):
    try:
        create_data = dict(create_data_payload)
        user = {
            "_id": create_data["firebase_id"],
            "first_name": None,
            "last_name": None,
            "nick_name": create_data["nick_name"],
            "email": create_data["email"],
            "phone_number": None,
            "cookie_number": 0,
            "result_list": [],
            "fav_stock": [],
            "strategy": []
            }
        conn.project.user.insert_one(user)
        response_data = usersEntity(conn.project.user.find())
        response = {
            "Status": "Successful",
            "Payload": response_data
        }
        return response
    except Exception as e:
        return {
            "Status": "Error",
            "Info": str(e)
        }

@user.put('/{id}')
async def update_user(id, user: User):
    try:
        conn.project.user.find_one_and_update({"_id": id}, {
            "$set":dict(user)
        })
        response_data = userEntity(conn.project.user.find_one({"_id": id}))
        response = {
            "Status": "Successful",
            "Payload": response_data
        }
        return response
    except Exception as e:
        return {
            "Status": "Error",
            "Info": str(e)
        }
'''
@user.patch('/{id}')
async def patch_user(id, info: User):
    conn.project.user.find_one_and_update(filter, update)
'''
@user.delete('/{id}')
async def delete_user(id):
    try:
        return {
            "Status": "Successful",
            "Payload": userEntity(conn.project.user.find_one_and_delete({"_id": id}))
        }
    except Exception as e:
        return {
            "Status": "Error",
            "Info": str(e)
        }