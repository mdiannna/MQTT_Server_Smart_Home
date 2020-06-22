from app import db



class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(30), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    # inside => true
    inside = db.Column(db.Boolean, nullable=False, default=True)
    


class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'),
        nullable=False)
    sensor = db.relationship('Sensor',
        backref=db.backref('sensordata', lazy=True))

    
    def __repr__(self):
        return '<User %r>' % self.username