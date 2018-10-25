from flask import Flask
from flask_cors import CORS
from sense_hat import SenseHat

app = Flask(__name__)
CORS(app)

@app.route("/temp")
def temp():
  sense = SenseHat()
  sense.clear()
  temp = sense.get_temperature()
  return temp

@app.route("/hello")
def helloWorld():
  return "Hello, cross-origin-world!"