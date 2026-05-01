from flask import Flask, render_template, request
from database import DatabaseDutyRepository, InMemoryDutyRepository
import json

app = Flask(__name__)

dabatase_location = "memory"

if dabatase_location == "memory":
  with open('seed_data/duties.json') as duties, open('seed_data/coins.json') as coins:
      db = InMemoryDutyRepository(json.load(duties), json.load(coins))
      
elif dabatase_location == "real_db":
  db = DatabaseDutyRepository()

@app.route('/')
def index():
  coins = db.list_all_coins()
  return render_template("index.html", coins=coins)

@app.route('/coin/<coin_id>')
def get_coin(coin_id):
  coin = db.get_coin_by_id(coin_id)
  duties = db.get_duties_by_number(coin["duties"])
  return render_template("coin.html", coin=coin, duties=duties)

@app.route('/coin/<coin_id>', methods=['POST'])
def add_duty_to_coin(coin_id):
  error = None
  try:
    duty_number = int(request.form.get("number"))
    duty_desc = request.form.get("description")
    error = False
    db.save_duty(duty_number, duty_desc)
    db.add_duty_to_coin(coin_id, duty_number)
    
  except ValueError:
    error = "Error: Duty number must be an integer"
  
  coin = db.get_coin_by_id(coin_id)
  duties = db.get_duties_by_number(coin["duties"])
  
  return render_template("coin.html", coin=coin, duties=duties, error=error)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
