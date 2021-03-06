from flask import Flask
from flask_mqtt import Mqtt
from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import json
import requests

app = Flask(__name__)
app.secret_key = "secret"

app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
app.config['MQTT_USERNAME'] = ''  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = ''  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 5  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/mdiannna/Code/MQTT_Server_Smart_Home/database.db"

db = SQLAlchemy(app)

migrate = Migrate(app, db)


manager = Manager(app)
manager.add_command('db', MigrateCommand)


mqtt = Mqtt(app)

from app import sensor_data

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('home/testtopic')


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print("------MQTT RECEIVE----")
    # payload = json.loads(msg.payload) # you can use json.loads to convert string to json

    # print(payload)
    res = requests.post('http://localhost:5000/post-sensor-data', json=data)
    print ('response from server:',res.text)
    dictFromServer = res.json()

    # # add_json_data(data["payload"])
    # # payload = copy(data["payload"])
    # # data_result = json.loads(str(payload))
    # data_result = json.dumps(str(payload))
    # print(data["payload"])

    # print(data_result)
    client.disconnect()



# Bootstrap(app)
from app import routes