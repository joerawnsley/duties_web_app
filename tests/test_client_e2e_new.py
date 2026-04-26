from app import app

test_app = app.test_client()

def test_home_page_has_content():
    response = test_app.get("/")
    assert "title" in response.text

def test_home_page_has_heading():
    response = test_app.get("/")
    assert "<h1>Devops Apprenticeship Coins</h1>" in response.text

def test_home_page_contains_link_to_automate_coin():
    response = test_app.get("/")
    assert "<a href='/automate'" in response.text or '<a href="/automate"' in response.text
    assert response.text.count("<li>") > 0