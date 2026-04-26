class Coin:
    pass

class CoinRepository:
        # superclass for defining how coin repository should behave
    def get_coin_by_name(self, name):
        pass
    def save_coin(salf, coin: Coin):
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
    pass