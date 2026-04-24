import os
import json
from dotenv import load_dotenv

load_dotenv()
DB_MODE = os.getenv("DB_MODE", "mock")

with open('mock_data/duties.json') as duties:
    mock_duties = json.load(duties)
    
def get_duties():
    if DB_MODE == "mock":
        return mock_duties
    else:
        pass
    
with open('mock_data/coins.json') as coins:
    mock_coins = json.load(coins)

def get_coins():
    if DB_MODE == "mock":
        return mock_coins
    else:
        pass