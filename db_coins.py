class CoinRepository:
        # superclass for defining how coin repository should behave
    def get_coin_by_name(self, name):
        pass
    def save_coin(self, name, id, duties):
        pass
    def delete_coin_by_name(self, name):
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
    
    