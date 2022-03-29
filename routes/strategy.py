from fastapi import APIRouter

from models.strategy import Strategy
from config.db import conn
from schemas.strategy import strategyEntity, strategiesEntity
from bson import ObjectId

strategy = APIRouter()

@strategy.get('/')
async def find_all_strategy():
    return strategiesEntity(conn.local.strategy.find())

@strategy.get('/{id}')
async def find_one_strategy(id):
    return strategyEntity(conn.local.strategy.find_one({'_id': ObjectId(id)}))

@strategy.post('/')
async def create_strategy(strategy: Strategy):
    conn.local.strategy.insert_one(dict(strategy))
    return strategiesEntity(conn.local.strategy.find())

@strategy.put('/{id}')
async def update_strategy(id, strategy: Strategy):
    conn.local.strategy.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(strategy)
    })
    return strategyEntity(conn.local.strategy.find_one({"_id": ObjectId(id)}))

@strategy.delete('/{id}')
async def delete_strategy(id):
    return strategyEntity(conn.local.strategy.find_one_and_delete({"_id": ObjectId(id)}))