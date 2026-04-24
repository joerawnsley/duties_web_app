from app import app
import webbrowser
from pathlib import Path
import json

test_app = app.test_client()

# load pages with mocked response
with open('mock_data/duties.json') as duties:
    mock_duties = json.load(duties)

def get_home_page(mocker):    
    mocker.patch("db.get_duties", return_value=mock_duties)
    response = test_app.get("/")
    return response

def get_automate_page(mocker):
    mocker.patch("db.get_duties", return_value=mock_duties)
    response = test_app.get("/automate")
    return response

# tests for home page
def test_home_page_has_page_content(mocker):
    assert "title" in get_home_page(mocker).text

def test_home_page_has_heading(mocker):
    assert "<h1>Devops Apprenticeship Coins</h1>" in get_home_page(mocker).text

def test_home_page_contains_link_to_automate_coin(mocker):
    assert "<a href='automate'>" in get_home_page(mocker).text or '<a href="automate">' in get_home_page(mocker).text
    assert get_home_page(mocker).text.count("<li>") > 0

# tests for automate page
def test_automate_page_has_heading(mocker):
    assert "<h1>Automate Coin</h1>" in get_automate_page(mocker).text

def test_automate_page_contains_form(mocker):
    page = get_automate_page(mocker).text
    assert "<form" in page
    assert "<button" in page
    assert "type='submit'" in page or 'type="submit"' in page
    assert "input" in page and "text" in page

# removed tests

def xtest_home_page_contains_duty_1_description(mocker):
    assert "Script and code" in get_home_page(mocker).text
    
def xtest_page_is_populated_with_duties_from_db(mocker):
    
    assert "Script and code" in get_home_page(mocker).text
    
def xtest_duty_identifiers_are_displayed_on_home_page(mocker):
    assert "Duty 1:" in get_home_page(mocker).text

def xtest_list_items_contain_links(mocker):
    assert "<li><a href=" in get_home_page(mocker).text