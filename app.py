from flask import Flask, render_template, request
import db_coins, db_duties
app = Flask(__name__)


@app.route('/')
def index():
  coins = db_coins.coins_repo.list_all_coins()
  return render_template("index.html", coins=coins)

@app.route('/coin/<coin_id>')
def get_coin(coin_id):
  coin = db_coins.coins_repo.get_coin_by_id(coin_id)
  duties = db_duties.duties_repo.get_duties_by_number(coin["duties"])
  return render_template("coin.html", coin=coin, duties=duties)

@app.route('/coin/<coin_id>', methods=['POST'])
def add_duty_to_coin(coin_id):
  
  duty_number = int(request.form.get("number"))
  duty_desc = request.form.get("description")

  db_duties.duties_repo.save_duty(duty_number, duty_desc)
  db_coins.coins_repo.add_duty_to_coin(coin_id, duty_number)
  
  coin = db_coins.coins_repo.get_coin_by_id(coin_id)
  duties = db_duties.duties_repo.get_duties_by_number(coin["duties"])
  
  return render_template("coin.html", coin=coin, duties=duties)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
