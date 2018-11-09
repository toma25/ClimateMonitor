from flask import render_template
from flask import Flask
from sense_hat import SenseHat

app = Flask(__name__)

@app.route("/temp")
def temp():
  sense = SenseHat()
  sense.clear()
  celcius = round(sense.get_temperature())
  humidity = round(sense.get_humidity())
  pressure = round(sense.get_pressure())
  temp_from_pressure = round(sense.get_temperature_from_pressure())

  climate = {'temp': celcius, 'temp_from_pressure':temp_from_pressure,  'humidity':humidity, 'pressure': pressure}
  return render_template('temp.html', title='Current climate', climate=climate)

@app.route("/hello")
def helloWorld():
  return "Hello, cross-origin-world!"