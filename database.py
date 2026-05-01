import json

class DutyRepository:
    # superclass for defining how duty repository should behave
    # duty methods
    def get_duties_by_number(self, numbers):
        pass
    def save_duty(self, number, description):
        pass
    def delete_duty_by_number(self, numbers):
        pass
    def list_all_duties(self):
        pass
    # coin methods
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
    
class DatabaseDutyRepository(DutyRepository):
    # placeholder for real db interaction logic
    pass

class InMemoryDutyRepository(DutyRepository):
    # in memory database to be used during development
    def __init__(self, duties, coins):
        self.duties = duties
        self.coins = coins

    def list_all_duties(self):
        return self.duties
    
    def list_all_coins(self):
        return self.coins
    
    def get_duties_by_number(self, numbers):
        # return a single duty when passed a number, or a list of duties when passed a list of numbers
        if type(numbers) == int:
            return list(filter(lambda duty: duty["number"] == numbers, self.duties))
        elif type(numbers) == list:
            return list(filter(lambda duty: duty["number"] in numbers, self.duties))
    
    def save_duty(self, number, description):
        new_duty = dict(number = number, description = description)
        update = False
        for existing_duty in self.duties:
            if existing_duty["number"] == new_duty["number"]:
                existing_duty["description"] = new_duty["description"]
                update = True
        if not update:
            self.duties.append(new_duty)
    
    def delete_duty_by_number(self, numbers):
        # delete a single duty when passed a number, or a list of duties when passed a list of numbers
        if type(numbers) == int:
            self.duties = list(filter(lambda duty: duty["number"] != numbers, self.duties))
        elif type(numbers) == list:
            self.duties = list(filter(lambda duty: duty["number"] not in numbers, self.duties))
    
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

