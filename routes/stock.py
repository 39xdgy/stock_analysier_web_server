from fastapi import APIRouter

from models.stock import Stock
from config.db import conn 
from schemas.stock import stockEntity, stocksEntity
from bson import ObjectId

import yfinance as yf
import stockstats

stock = APIRouter()

@stock.get('/')
async def find_all_stock():
    return stocksEntity(conn.local.stock.find())

@stock.get('/{id}')
async def find_one_stock_id(id):
    return stockEntity(conn.local.stock.find_one({"_id": ObjectId(id)}))


@stock.get('/name/{name}')
async def find_one_stock_name(name):
    return stockEntity(conn.local.stock.find_one({"name": name}))


@stock.post('/')
async def create_stock(stock: Stock):
    conn.local.stock.insert_one(dict(stock))
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

@stock.post('/update_stock_data')
async def update_stock_data(): # TODO per stock or all stock
    pass

@stock.post('/create_default_data')
async def create_default_data():
    all_ticker = []
    
    for file_name in ['nasdaqlisted.txt', 'otherlisted.txt']:
        all_data = open(f'files/{file_name}', 'r')
        for line in all_data:
            info = line.split("|")
            ticker = info[0]
            if 'File Creation Time' not in ticker and 'Symbol' not in ticker and "$" not in ticker and "." not in ticker and ticker not in all_ticker:
                all_ticker.append(ticker)
    print(len(all_ticker))

    # Testing
    all_ticker = ['aapl', 'zm']

    for ticker in all_ticker:
        ticker_obj = yf.Ticker(ticker)
        stock_data = yf.download(ticker, period = '7d', interval = '1m')
        # TODO would grab data from indicator database for creating all the data
        stockStat = stockstats.StockDataFrame.retype(stock_data)
        
        for indicator_name in ['macd', 'kdjk', 'kdjd', 'kdjj']:
            stock_data[indicator_name] = stockStat[[indicator_name]]
        
        category = 'N/A'
        link = 'N/A'
        if 'sector' in ticker_obj.info: category = ticker_obj.info['sector']
        if 'website' in ticker_obj.info: link = ticker_obj.info['website']
        stock_data.index = stock_data.index.astype(str)
        conn.local.stock.insert_one({
            'name': ticker,
            'category': category,
            'link': link,
            'data': stock_data.T.to_dict()
        })

    return {"status": "Success"}