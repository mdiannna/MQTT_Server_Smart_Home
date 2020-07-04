from app import app
from flask import render_template, request, redirect, url_for, jsonify, make_response
from app import mqtt
from app.models import Sensor, SensorData
from app import db 
from app.sensor_data import add_json_data, aggregate_sensor_data
from sqlalchemy import desc


@app.route('/')
def hello():
    # mqtt.publish('home/testtopic', 'hello world')
    message = '{"v": 10.2, "t": "h",  "id": "sensor1", "ts": "04-03-12 12:00"}'
    mqtt.publish('home/testtopic', message)

    data = SensorData.query.limit(20).all()

    return render_template("index.html", data=data)


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
            inside =   True if inside=="inside" else False
            sensor = Sensor(location=location, type=s_type, inside=inside)
            db.session.add(sensor)
            db.session.commit()
        return redirect('/manage-sensors')
        # TODO:
        # sensor = Sensor(location='Room1Left', type="", inside=True)
    return render_template('add_sensor.html')

@app.route('/delete-sensor', methods=['DELETE', 'POST'])
def delete_sensor():


    sensor = Sensor.query.get(request.form['sensor_id'])
    db.session.delete(sensor)
    db.session.commit()
    # flash('Entry deleted')
    # res = make_response(jsonify({}), 204)
    # return res
    return redirect('manage-sensors')




@app.route('/manage-sensors')
def manage_sensors():
    sensors = Sensor.query.all()
    return render_template("manage_sensors.html", data=sensors)


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



@app.route('/health_page')
def health_page():
    
    return render_template("health_page.html")


@app.route('/last-sensor-data')
def get_last_sensor_data():

    sensor_data = SensorData.query.order_by(desc(SensorData.timestamp)).limit(1).first()
    print(sensor_data)
    # print(sensor_data[0].value)
    return str(sensor_data)



@app.route('/last-sensors-data-aggregated')
def get_last_sensors_data_aggregated():

    sensor_data = SensorData.query.order_by(desc(SensorData.timestamp)).limit(3).all()
    print(sensor_data)
    # print(sensor_data[0].value)
    sensors_data_aggregated = aggregate_sensor_data(sensor_data)
    return sensors_data_aggregated


@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/team')
def team():
    return render_template("team.html")
