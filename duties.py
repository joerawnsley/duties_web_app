class Duty:
    pass

class DutyRepository:
    # superclass for defining how duty repository should behave
    def get_duty_by_number(self, number):
        pass
    def save_duty(self, duty: Duty):
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
    pass

