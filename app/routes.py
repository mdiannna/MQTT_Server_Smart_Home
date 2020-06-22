from app import app
from flask import render_template, request, redirect
from app import mqtt
from app.models import Sensor, SensorData
from app import db 
@app.route('/')
def hello():
	mqtt.publish('home/testtopic', 'hello world')

	return render_template("index.html")


@app.route('/add-sensor', methods=["GET", "POST"])
def add_sensor():
	if request.method=="POST":
		
		# if request.form["type"]:
		s_type = request.form.get("type")
		location = request.form.get("location")
		inside = request.form.get("inside")

		print(s_type)
		print(location)
		print(inside)

		if (s_type != "") and (inside != None) and (location != ""):
			inside =   True if "inside" else False
			sensor = Sensor(id=1, location=location, type=s_type, inside=inside)
			db.session.add(sensor)
			db.session.commit()
		
		# TODO:
		# sensor = Sensor(location='Room1Left', type="", inside=True)
	return render_template('add_sensor.html')


# TODO
# def add_sensor_data(data):
# 	sensor = Sensor(location='Room1Left', type="", inside=True)
# 	sensor_data = SensorData(value=, type="", timestamp=)
	
# 	sensor.sensordata.append(sensor_data)	
# 	db.session.add(sensor)
