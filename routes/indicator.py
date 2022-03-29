from fastapi import APIRouter

from models.indicator import Indicator
from config.db import conn
from schemas.indicator import indicatorEntity, indicatorsEntity
from bson import ObjectId

indicator = APIRouter()

@indicator.get('/')
async def find_all_indicator():
    return indicatorsEntity(conn.local.indicator.find())

@indicator.get('/{id}')
async def find_one_indicator(id):
    return indicatorEntity(conn.local.indicator.find_one({'_id': ObjectId(id)}))

@indicator.post('/')
async def create_indicator(indicator: Indicator):
    conn.local.user.insert_one(dict(indicator))
    return indicatorsEntity(conn.local.indicator.find())

@indicator.put('/{id}')
async def update_indicator(id, indicator: Indicator):
    conn.local.indicator.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(indicator)
    })
    return indicatorEntity(conn.local.indicator.find_one({"_id": ObjectId(id)}))

@indicator.delete('/{id}')
async def delete_indicator(id):
    return indicatorEntity(conn.local.indicator.find_one_and_delete(filter))