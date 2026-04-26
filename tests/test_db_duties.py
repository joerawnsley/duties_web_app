from db_duties import InMemoryDutyRepository
import json
import pytest

with open('seed_data/duties.json') as duties:
    seed_data = json.load(duties)

@pytest.fixture
def duties_repo():
    duties_repo = InMemoryDutyRepository(seed_data)
    return duties_repo

def test_repository_lists_all_duties(duties_repo):
    all_duties = duties_repo.list_all_duties()
    assert all_duties == seed_data
    
def test_repository_lists_single_specified_duty(duties_repo):
    duty_2 = duties_repo.get_duties_by_number(2)
    duty_3 = duties_repo.get_duties_by_number(3)
    assert duty_2 == [{ "number": 2, "description": "Deploy continuously" }]
    assert duty_3 == [{ "number": 3, "description": "Automate stuff" }]
    
def test_repository_returns_list_of_duties_by_number(duties_repo):
    duty_1_and_3 = duties_repo.get_duties_by_number([1, 3])
    assert duty_1_and_3 == [
        { "number": 1, "description": "Script and code" },
        { "number": 3, "description": "Automate stuff" }
        ]
    