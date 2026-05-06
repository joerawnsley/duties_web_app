from database import InMemoryDutyRepository
import json
import pytest
from copy import deepcopy

# these are unit tests for the in-memory database. They use a fixture to create a copy of the database so that each test is isolated and doesn't affect other tests

with open('seed_data/duties.json') as duties, open('seed_data/coins.json') as coins:
    seed_duties = json.load(duties)
    seed_coins = json.load(coins)
    db = InMemoryDutyRepository(seed_duties, seed_coins)

@pytest.fixture
def db_copy():
    return deepcopy(db)

# duties

def test_repository_lists_all_duties(db_copy):
    all_duties = db_copy.list_all_duties()
    assert all_duties == seed_duties
    
def test_repository_lists_single_specified_duty(db_copy):
    duty_2 = db_copy.get_duties_by_number(2)
    duty_3 = db_copy.get_duties_by_number(3)
    assert duty_2 == [{ "number": 2, "description": "Deploy continuously" }]
    assert duty_3 == [{ "number": 3, "description": "Automate stuff" }]
    
def test_repository_returns_list_of_duties_by_number(db_copy):
    duty_1_and_3 = db_copy.get_duties_by_number([1, 3])
    assert duty_1_and_3 == [
        { "number": 1, "description": "Script and code" },
        { "number": 3, "description": "Automate stuff" }
        ]

def test_saving_a_duty_adds_to_repository(db_copy):
    db_copy.save_duty(4, "Respond to changing requirements")
    assert db_copy.list_all_duties() == [
    { "number": 1, "description": "Script and code" },
    { "number": 2, "description": "Deploy continuously" },
    { "number": 3, "description": "Automate stuff" },
    { "number": 4, "description": "Respond to changing requirements" }
    ]
    
def test_delete_duty_removes_single_duty_from_repository(db_copy):
    db_copy.delete_duty_by_number(1)
    assert db_copy.list_all_duties() == [
    { "number": 2, "description": "Deploy continuously" },
    { "number": 3, "description": "Automate stuff" },
]
    
def test_delete_duty_removes_list_of_duties(db_copy):
    db_copy.delete_duty_by_number([2, 1])
    assert db_copy.list_all_duties() == [
        {"number": 3, "description": "Automate stuff"}
    ]

def test_saving_a_duty_with_existing_id_updates_the_duty(db_copy):
    db_copy.save_duty(3, "Automate everything!")
    assert db_copy.list_all_duties() == [
    { "number": 1, "description": "Script and code" },
    { "number": 2, "description": "Deploy continuously" },
    { "number": 3, "description": "Automate everything!" },
    ]

# coins

def test_repository_lists_all_coins(db_copy):
    all_coins = db_copy.list_all_coins()
    assert all_coins == seed_coins

def test_save_coin_adds_coin_to_repo(db_copy):
    db_copy.save_coin("Houston, Prepare to Launch", "houston", [5, 7, 10]
    )
    assert db_copy.list_all_coins() == [
         {
        "name": "Automate!",
        "id": "automate",
        "duties": []
    },
         {
        "name": "Call Security",
        "id": "security",
        "duties": [1, 2, 3]
    },
    {
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    }
    ]

def test_delete_coin_removes_coin_from_repo(db_copy):
    db_copy.save_coin("Houston, Prepare to Launch", "houston", [5, 7, 10]
    )
    db_copy.delete_coin_by_id("automate")
    assert db_copy.list_all_coins() == [
         {
        "name": "Call Security",
        "id": "security",
        "duties": [1, 2, 3]
    },
         {
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    }
    ]

def test_get_coin_by_id_returns_single_coin(db_copy):
    db_copy.save_coin("Houston, Prepare to Launch", "houston", [5, 7, 10]
    )
    assert db_copy.get_coin_by_id("houston") == {
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    }

def test_add_duty_adds_new_duty(db_copy):
    db_copy.add_duty_to_coin("automate", 1)
    assert db_copy.list_all_coins() == [
    {
        "name": "Automate!",
        "id": "automate",
        "duties": [1]
    },
    {
        "name": "Call Security",
        "id": "security",
        "duties": [1, 2, 3]
    }
]

def test_add_duty_does_not_add_duty_if_already_exists(db_copy):
    db_copy.add_duty_to_coin("security", 2)
    assert db_copy.list_all_coins() == [
    {
        "name": "Automate!",
        "id": "automate",
        "duties": []
    },
    {
        "name": "Call Security",
        "id": "security",
        "duties": [1, 2, 3]
    }
]