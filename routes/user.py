from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId 


user = APIRouter()

@user.get('/')
async def find_all_user():
    #print(conn.project.user.find())  address of the object
    #print(usersEntity(conn.project.user.find()))   actual data
    return usersEntity(conn.project.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return userEntity(conn.project.user.find_one({'_id': ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    conn.project.user.insert_one(dict(user))
    return usersEntity(conn.project.user.find())

@user.put('/{id}')
async def update_user(id, user: User):
    conn.project.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set":dict(user)
    })
    return userEntity(conn.project.user.find_one({"_id": ObjectId(id)}))
'''
@user.patch('/{id}')
async def patch_user(id, info: User):
    conn.project.user.find_one_and_update(filter, update)
'''
@user.delete('/{id}')
async def delete_user(id):
    return userEntity(conn.project.user.find_one_and_delete({"_id": ObjectId(id)}))