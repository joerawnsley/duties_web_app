from flask import Flask

app = Flask(__name__)

@app.route('/')
def list_duties(duties):
  if duties:
    return '<h1><center>Duty 1</center></h1>'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
