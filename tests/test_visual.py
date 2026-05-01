from app import app
import webbrowser
from pathlib import Path
import json

test_app = app.test_client()

# get home page with mock data
def get_home_page(mocker):    
    mocker.patch('app.db.list_all_coins', return_value=[
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
    return response

# get automate page with mock data
def get_automate_page(mocker):
    mocker.patch('app.db.get_coin_by_id', return_value={
        "name": "Automate!",
        "id": "automate",
        "duties": [5, 7, 10]
    })
    response = test_app.get("/automate")
    return response


# visual check for homepage
def xtest_display_home_page(mocker):
    html_content = get_home_page(mocker).text
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / "home_page_preview.html"
    file_path.write_text(html_content)
    webbrowser.open(f"file://{file_path.absolute()}")
    assert file_path.exists()
    
    # visual check for automate page
def xtest_display_automate_page(mocker):
    html_content = get_automate_page(mocker).text
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / "automate_page_preview.html"
    file_path.write_text(html_content)
    webbrowser.open(f"file://{file_path.absolute()}")
    assert file_path.exists()