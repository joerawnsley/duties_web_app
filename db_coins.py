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
    
    
    
    