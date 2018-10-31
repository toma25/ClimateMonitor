from flask import render_template
from flask import Flask
from sense_hat import SenseHat

app = Flask(__name__)

@app.route("/temp")
def temp():
  sense = SenseHat()
  sense.clear()
  celcius = int(round(sense.get_temperature()))
  humidity = int(round(sense.get_humidity()))
  pressure = int(round(sense.get_pressure()))

  climate = {'temp': str(celcius), 'humidity':humidity, 'pressure': pressure}
  return render_template('temp.html', title='Current climate', climate=climate)

@app.route("/hello")
def helloWorld():
  return "Hello, cross-origin-world!"