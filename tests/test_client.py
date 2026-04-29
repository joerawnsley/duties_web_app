from app import app
from db_duties import duties_repo, seed_db_in_memory

# these are integration tests as they test how the app integrates with templates, given a mock resopnse from the db

test_app = app.test_client()

# ----------------- home page -------------
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
    assert "<a href='/coin/automate'" in response.text or '<a href="/coin/automate"' in response.text
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
    assert "<a href='/coin/automate'" not in response.text and '<a href="/coin/automate"' not in response.text
    assert "<a href='/coin/houston'" in response.text or '<a href="/coin/houston"' in response.text
    assert response.text.count("<li>") > 1
    
def test_home_page_notifies_user_if_coins_not_available(mocker):
    mocker.patch("db_coins.coins_repo.list_all_coins", return_value=None)
    response = test_app.get("/")
    assert "<a href='/automate'" not in response.text and '<a href="/automate"' not in response.text
    assert "There are no coins to display" in response.text
    assert response.text.count("<li>") == 0
    
# --------- coin pages ---------

def test_automate_page_has_heading():
    response = test_app.get("coin/automate")
    assert "<h1>Coin: Automate!</h1>" in response.text

def test_houston_page_has_heading(mocker):
    mocker.patch('db_coins.coins_repo.get_coin_by_id', return_value={
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    })
    response = test_app.get("coin/houston")
    assert "<h1>Coin: Houston, Prepare to Launch</h1>" in response.text
    
def test_houston_page_has_duties(mocker):
    mocker.patch('db_coins.coins_repo.get_coin_by_id', return_value={
        "name": "Houston, Prepare to Launch",
        "id": "houston",
        "duties": [5, 7, 10]
    })
    mocker.patch('db_duties.duties_repo.get_duties_by_number', return_value=[
        { "number": 5, "description": "Build and operate" },
        { "number": 7, "description": "Provision cloud infrastructure" },
        { "number": 10, "description": "Implement monitoring" }
    ])
    response = test_app.get("coin/houston")
    assert "<li><b>Duty 5:</b> Build and operate</li>" in response.text
    assert response.text.count("<li>") == 3
    
# ------POST route-----------

def test_form_submit_displays_new_duties():
    response = test_app.get("coin/automate")
    assert "<li><b>Duty 1:</b> Script and code</li>" not in response.text
    response = test_app.post("coin/automate", data={"number": "1", "description": "Script and code"})
    assert "<li><b>Duty 1:</b> Script and code</li>" in response.text


def test_form_submit_updates_duties():
    response = test_app.get("coin/security")
    assert "<li><b>Duty 1:</b> Script and code</li>" in response.text
    response = test_app.post("coin/security", data={"number": "1", "description": "Script and script some more"})
    assert "<li><b>Duty 1:</b> Script and code</li>" not in response.text
    assert "<li><b>Duty 1:</b> Script and script some more</li>" in response.text
    duties_repo.save_duty(1, "Script and code")

    
def test_post_route_adds_duty_to_existing_duties(mocker):
    print("hello")
    print(duties_repo.list_all_duties())
    mocker.patch('db_coins.coins_repo.get_coin_by_id', return_value={
        "name": "Call Security",
        "id": "security",
        "duties": [1, 2, 4]
    })
    response = test_app.post("coin/security", data={"number": "4", "description": "Continuously integrate"})
    assert "<li><b>Duty 1:</b> Script and code</li>" in response.text
    assert "<li><b>Duty 2:</b> Deploy continuously</li>" in response.text
    assert "<li><b>Duty 3:</b>" not in response.text
    assert "<li><b>Duty 4:</b> Continuously integrate</li>" in response.text