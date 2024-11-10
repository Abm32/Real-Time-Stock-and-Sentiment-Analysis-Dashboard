import pymongo
from config import MONGODB_URI

# Connect to MongoDB
client = pymongo.MongoClient(MONGODB_URI)
db = client['stock_analysis']
stock_data_collection = db['historical_stock_data']

def get_historical_data(symbol):
    # Fetch historical data for the given stock symbol
    return list(stock_data_collection.find({"symbol": symbol}))
