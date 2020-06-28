from app import app
from flask import render_template, request, redirect, url_for, jsonify
from app import mqtt
from app.models import Sensor, SensorData
from app import db 
from app.sensor_data import add_json_data

@app.route('/')
def hello():
    # mqtt.publish('home/testtopic', 'hello world')
    message = '{"v": 10.2, "t": "h",  "id": "sensor1", "ts": "04-03-12 12:00"}'
    mqtt.publish('home/testtopic', message)

    return render_template("index.html")


@app.route('/post-sensor-data', methods=["GET", "POST"])
def post_sensor_data():
    if request.method=="POST":
        input_json = request.get_json(force=True) 

        print ('data from client:', input_json)
        add_json_data(input_json["payload"])
        print("post!!!")
        dictToReturn = {'status': "received"}
        return jsonify(dictToReturn)

    else:
        print("get!")
    return "OK"

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



@app.route('/health_state', methods=["GET", "POST"])
def post_health_state():
    if request.method=="POST":
        input_json = request.get_json(force=True) 

        # daca parametri in request:
        # feeling = request.form.get("feeling")
        # daca forlosim JSON:
        # feeling trebuie sa fie 1, 2, 3 sau trebuie de convertit!!!!
        feeling = input_json["feeling"]


        userData = UserData(user_id=1, feeling=feeling)
        db.session.add(userData)
        db.session.commit()

        dictToReturn = {'status': "received"}
        return jsonify(dictToReturn)
    else:
        print("get!")
    return "OK"