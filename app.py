from flask import Flask, render_template
import db
from db_duties import InMemoryDutyRepository, DatabaseDutyRepository
from db_coins import InMemoryCoinRepository, DatabaseCoinRepository
app = Flask(__name__)
import json

dabatase_location = "memory"

if dabatase_location == "memory":
  with open('seed_data/duties.json') as duties:
      duties_repo = InMemoryDutyRepository(json.load(duties))
  with open('seed_data/coins.json') as duties:
      coins_repo = InMemoryCoinRepository(json.load(duties))

elif dabatase_location == "real_db":
  duties_repo = DatabaseDutyRepository()
  coins_repo = DatabaseCoinRepository()


@app.route('/')
def index():
  coins = db.get_coins()
  return render_template("index.html", coins=coins)

@app.route('/automate')
def automate():
  return render_template("automate.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
