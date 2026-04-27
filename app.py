from flask import Flask, render_template, request
import db_coins, db_duties
from db_duties import InMemoryDutyRepository, DatabaseDutyRepository
from db_coins import InMemoryCoinRepository, DatabaseCoinRepository
app = Flask(__name__)


@app.route('/')
def index():
  coins = db_coins.coins_repo.list_all_coins()
  return render_template("index.html", coins=coins)

# @app.route('/automate')
# def automate():
#   return render_template("automate.html")

# @app.route('/security')
# def security():
#   return render_template("security.html")

# @app.route('/houston')
# def houston():
#   return render_template("houston.html")

# @app.route('/deeper')
# def deeper():
#   return render_template("deeper.html")

@app.route('/<coin_id>')
def coin(coin_id):
  coin = db_coins.coins_repo.get_coin_by_id(coin_id)
  return render_template("coin.html", coin=coin)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
