import json

class CoinRepository:
        # superclass for defining how coin repository should behave
    def get_coin_by_id(self, id):
        pass
    def save_coin(self, name, id, duties):
        pass
    def delete_coin_by_id(self, id):
        pass
    def list_all_coins(self):
        pass
    def add_duty_to_coin(self):
        pass
    
class DatabaseCoinRepository(CoinRepository):
    # placeholder for real db interaction logic
    pass

class InMemoryCoinRepository(CoinRepository):
    # in memory database to be used during development
    def __init__(self, coins):
        self.coins = coins
    
    def list_all_coins(self):
        return self.coins

    def save_coin(self, name, id, duties):
        new_coin = dict(name=name, id=id, duties=duties)
        self.coins.append(new_coin)
    
    def delete_coin_by_id(self, id):
        self.coins = list(filter(lambda coin: coin["id"] != id, self.coins))
    
    def get_coin_by_id(self, id):
        return list(filter(lambda coin: coin["id"] == id, self.coins))[0]
    
    def add_duty_to_coin(self, coin_id, duty_number):
        for coin in self.coins:
            if coin["id"] == coin_id and duty_number not in coin["duties"]:
                coin["duties"].append(duty_number)
                coin["duties"].sort()
    
dabatase_location = "memory"

if dabatase_location == "memory":
    with open('seed_data/coins.json') as coins:
        coins_repo = InMemoryCoinRepository(json.load(coins))

elif dabatase_location == "real_db":
    coins_repo = DatabaseCoinRepository()