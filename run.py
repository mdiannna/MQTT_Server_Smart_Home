from app import app, manager
# import mqtt_handling

if __name__ =='__main__':	

	#app.run(host='0.0.0.0')
	# manager.run()
	# manager.run(debug=True, use_reloader=False)
	app.run(debug=True, use_reloader=False, host='0.0.0.0')
	# socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)




