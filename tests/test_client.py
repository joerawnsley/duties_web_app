from app import app

test_app = app.test_client()

def test_home_page_has_content():
    response = test_app.get("/")
    assert "title" in response.text

def test_home_page_has_heading():
    response = test_app.get("/")
    assert "<h1>Devops Apprenticeship Coins</h1>" in response.text

def test_home_page_contains_link_to_automate_coin(mocker):
    mocker.patch("db_coins.coins_repo.list_all_coins", return_value=[
    {
        "name": "Automate!",
        "id": "automate",
        "duties": []
    },
    {
        "name": "Call Security",
        "id": "security",
        "duties": [8, 9, 11]
    }
])
    response = test_app.get("/")
    assert "<a href='/automate'" in response.text or '<a href="/automate"' in response.text
    assert response.text.count("<li>") > 1

def test_number_of_links_on_home_page_matches_number_of_coins(mocker):
    mocker.patch("db_coins.coins_repo.list_all_coins", return_value=[
    {
        "name": "Automate!",
        "id": "automate",
        "duties": []
    },
    {
        "name": "Call Security",
        "id": "security",
        "duties": [8, 9, 11]
    },
    {
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    },
    {
        "name": "Going Deeper",
        "id": "deeper",
        "duties": [11]
    }
    ])
    response = test_app.get("/")
    assert response.text.count("<li>") == 4
    assert response.text.count("a href") == 4

def test_home_page_only_contains_links_to_coins_provided_by_db(mocker):
    mocker.patch("db_coins.coins_repo.list_all_coins", return_value=[
    {
        "name": "Call Security",
        "id": "security",
        "duties": [8, 9, 11]
    },
    {
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    }
])
    response = test_app.get("/")
    assert "<a href='/automate'" not in response.text and '<a href="/automate"' not in response.text
    assert "<a href='/houston'" in response.text or '<a href="/houston"' in response.text
    assert response.text.count("<li>") > 1
    
def test_home_page_notifies_user_if_coins_not_available(mocker):
    mocker.patch("db_coins.coins_repo.list_all_coins", return_value=None)
    response = test_app.get("/")
    assert "<a href='/automate'" not in response.text and '<a href="/automate"' not in response.text
    assert "There are no coins to display" in response.text
    assert response.text.count("<li>") == 0