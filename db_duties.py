class DutyRepository:
    # superclass for defining how duty repository should behave
    def get_duties_by_number(self, numbers):
        pass
    def save_duty(self, number, description, ksbs):
        pass
    def delete_duty_by_number(self, number):
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
        return [self.duties[1]]
