from app import app
from flask import render_template, request, redirect
from app import mqtt

@app.route('/')
def hello():
	mqtt.publish('home/testtopic', 'hello world')

	return render_template("index.html")