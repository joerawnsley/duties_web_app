from db_coins import InMemoryCoinRepository
import json
import pytest
from copy import deepcopy

with open('seed_data/coins.json') as coins:
    seed_data = json.load(coins)

@pytest.fixture
def coins_repo():
    coins_repo = InMemoryCoinRepository(deepcopy(seed_data))
    return coins_repo

def test_repository_lists_all_coins(coins_repo):
    all_coins = coins_repo.list_all_coins()
    assert all_coins == seed_data

def test_save_coin_adds_coin_to_repo(coins_repo):
    coins_repo.save_coin("Houston, Prepare to Launch", "houston", [5, 7, 10]
    )
    assert coins_repo.list_all_coins() == [
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

def test_delete_coin_removes_coin_from_repo(coins_repo):
    coins_repo.save_coin("Houston, Prepare to Launch", "houston", [5, 7, 10]
    )
    coins_repo.delete_coin_by_id("automate")
    assert coins_repo.list_all_coins() == [
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

def test_get_coin_by_id_returns_single_coin(coins_repo):
    coins_repo.save_coin("Houston, Prepare to Launch", "houston", [5, 7, 10]
    )
    assert coins_repo.get_coin_by_id("houston") == {
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    }

def test_add_duty_adds_new_duty(coins_repo):
    coins_repo.add_duty_to_coin("automate", 1)
    assert coins_repo.list_all_coins() == [
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

def test_add_duty_does_not_add_duty_if_already_exists(coins_repo):
    coins_repo.add_duty_to_coin("security", 2)
    assert coins_repo.list_all_coins() == [
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