from flask import Flask
from sense_hat import SenseHat

app = Flask(__name__)

@app.route("/temp")
def temp():
  sense = SenseHat()
  sense.clear()
  celcius = int(round(sense.get_temperature()))
  return str(celcius)

@app.route("/hello")
def helloWorld():
  return "Hello, cross-origin-world!"