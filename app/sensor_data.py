
# TODO

import json
from app import db 
from datetime import datetime

from app.models import Sensor, SensorData

def add_sensor_data(data):
	if (("v" in data) and ("t" in data) and ("id" in data) and ("ts" in data)):
		print("ok!")

		value = data["v"]
		s_type = data["t"]
		sensor_id = data["id"]
		# timestamp = data["ts"]
		timestamp = datetime.now()

		# sensor = Sensor(location='Room1Left', type="", inside=True)
		sensor_data = SensorData(value=value, type=s_type, timestamp=timestamp, sensor_id=sensor_id)
		
		# sensor.sensordata.append(sensor_data)	
		db.session.add(sensor_data)
		db.session.commit()
	else:
		print("Error! JSON FORMAT NOT CORRECT!")
	


def json_to_data(data):
	# data format:
	# '{"v": 10.2, "t": "h",  "id": "sensor1", "ts": "04-03-12 12:00"}'	

	data_result = json.loads(data)
	print(data_result)
	return data_result


def add_json_data(data):
	add_sensor_data(json_to_data(data))


## Exemplu de utilizare:
# test_data = '{"v": 10.2, "t": "h",  "id": "sensor1", "ts": "04-03-12 12:00"}'	
# mydata = json_to_data(test_data)
# print(mydata)
# print(mydata["v"])
# print(mydata["t"])
# print(mydata["id"])
# print(mydata["ts"])