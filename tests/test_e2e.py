import re
from playwright.sync_api import Page, expect

url = "http://127.0.0.1:5000"

# these are end-to-end tests, testing different user journeys as they navigate through the app

def test_returns_status_200(page: Page):
    response = page.request.get(url)
    expect(response).to_be_ok()
    
def test_has_title(page: Page):
    page.goto(url)

    expect(page).to_have_title(re.compile("Apprenticeship"))
    
def test_navigation_to_coin_page_with_title(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Automate!").click()
    expect(page).to_have_title("Automate!")
    
def test_navigation_to_coin_page_with_url(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Call Security").click()
    expect(page).to_have_url(re.compile('coin/security'))

def test_navigation_to_coin_page_with_form(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Call Security").click()
    expect(page).to_have_url(re.compile('coin/security'))
    
def test_submitting_duty_displays_the_duty(page: Page):
    page.set_default_timeout(5000)
    page.goto(url)
    page.get_by_role("link", name="Automate!").click()
    
    page.get_by_label("number").fill("1")
    page.get_by_label("description").fill("Script and code")
    
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Duty 1: Script and code")).to_be_visible()
    
def test_duties_can_be_updated(page: Page):
    page.set_default_timeout(5000)
    page.goto(url)
    page.get_by_role("link", name="Call Security").click()
    expect(page.get_by_text("Duty 1: Script and code")).to_be_visible()
    expect(page.get_by_text("Duty 1: Script and script again")).not_to_be_visible()

    page.get_by_label("number").fill("1")
    page.get_by_label("description").fill("Script and script again")
    
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Duty 1: Script and script again")).to_be_visible()


def test_duties_can_be_added(page: Page):
    page.set_default_timeout(5000)
    page.goto(url + "/coin/security")
    expect(page.get_by_role("listitem")).to_have_count(3)
    
    page.get_by_label("number").fill("7")
    page.get_by_label("description").fill("Build and operate")
    page.get_by_role("button", name="Submit").click()
    
    expect(page.get_by_role("listitem")).to_have_count(4)
    
def test_duty_number_validation(page: Page):
    page.set_default_timeout(5000)
    page.goto(url + "/coin/security")
    original_duty_count = page.get_by_role("listitem").count()
    
    page.get_by_label("number").fill("Build and operate")
    page.get_by_label("description").fill("Build and operate")
    page.get_by_role("button", name="Submit").click()
    
    expect(page).to_have_url(re.compile('coin/security'))
    expect(page.get_by_role("listitem")).to_have_count(original_duty_count)
    expect(page.get_by_text("Error")).to_be_visible()


    
