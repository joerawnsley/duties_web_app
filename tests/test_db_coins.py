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
        "duties": [1, 5, 6, 7, 11, 13]
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
    coins_repo.delete_coin_by_name("automate")
    assert coins_repo.list_all_coins() == [
         {
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    }
    ]