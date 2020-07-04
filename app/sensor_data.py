
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


def aggregate_sensor_data(data):
    response = {"temperature":0, "humidity":0, "gas":0, "health_status":0, "timestamp":"0"}
    # response = {"temperature":0, "humidity":0, "gas":0}
    print(data)

    for item in data:
        if item.type=='t':
            response["temperature"] = item.value
        elif item.type=='h':
            response["humidity"] = item.value
        elif item.type=='g':
            response["gas"] = item.value

    response["timestamp"] = data[2].timestamp

    # [{"sensor_id": sensor1, "type": h, "value": 10.2, "timestamp": 2020-07-04 10:58:11.181771}, {"sensor_id": sensor1, "type": h, "value": 10.2, "timestamp": 2020-07-04 10:45:02.914721}, {"sensor_id": sensor1, "type": h, "value": 10.2, "timestamp": 2020-06-28 13:54:52.553669}]
    return response


## Exemplu de utilizare:
# test_data = '{"v": 10.2, "t": "h",  "id": "sensor1", "ts": "04-03-12 12:00"}' 
# mydata = json_to_data(test_data)
# print(mydata)
# print(mydata["v"])
# print(mydata["t"])
# print(mydata["id"])
# print(mydata["ts"])