from fastapi import APIRouter

from models.stock import Stock
from config.db import conn 
from schemas.stock import stockEntity, stocksEntity
from bson import ObjectId


stock = APIRouter()

@stock.get('/')
async def find_all_stock():
    return stocksEntity(conn.local.stock.find())

@stock.get('/{id}')
async def find_one_stock_id(id):
    return stockEntity(conn.local.stock.find_one({"_id": ObjectId(id)}))

''' #get stock by name
@stock.get('/')
'''

@stock.post('/')
async def create_stock(stock: Stock):
    conn.local.user.insert_one(dict(stock))
    return stocksEntity(conn.local.stock.find())

@stock.put('/{id}')
async def update_stock(id, stock: Stock):
    conn.local.stock.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(stock)
    })
    return stockEntity(conn.local.stock.find_one({"_id": ObjectId}))

@stock.delete('/{id}')
async def delete_stock(id):
    return stockEntity(conn.local.stock.find_one_and_delete({"_id": ObjectId(id)}))