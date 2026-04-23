from flask import Flask, render_template
import db
app = Flask(__name__)



@app.route('/')
def index():
  duties = db.get_duties()
  return render_template("index.html", duties=duties)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
