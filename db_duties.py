class DutyRepository:
    # superclass for defining how duty repository should behave
    def get_duties_by_number(self, numbers):
        pass
    def save_duty(self, number, description):
        pass
    def delete_duty_by_number(self, numbers):
        pass
    def list_all_duties(self):
        pass
    
class DatabaseDutyRepository(DutyRepository):
    # placeholder for real db interaction logic
    pass

class InMemoryDutyRepository(DutyRepository):
    # in memory database to be used during development
    def __init__(self, seed_data):
        self.duties = seed_data

    def list_all_duties(self):
        return self.duties
    
    def get_duties_by_number(self, numbers):
        # return a single duty when passed a number, or a list of duties when passed a list of numbers
        if type(numbers) == int:
            return list(filter(lambda duty: duty["number"] == numbers, self.duties))
        elif type(numbers) == list:
            return list(filter(lambda duty: duty["number"] in numbers, self.duties))
    
    def save_duty(self, number, description):
        new_duty = dict(number = number, description = description)
        self.duties.append(new_duty)
    
    def delete_duty_by_number(self, numbers):
        # delete a single duty when passed a number, or a list of duties when passed a list of numbers

        if type(numbers) == int:
            self.duties = list(filter(lambda duty: duty["number"] != numbers, self.duties))
        elif type(numbers) == list:
            self.duties = list(filter(lambda duty: duty["number"] not in numbers, self.duties))
