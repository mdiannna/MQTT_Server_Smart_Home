import pickle
import numpy as np

# filename = 'models/logreg_model.sav'
filename = 'app/models/logreg_model.sav'

model = pickle.load(open(filename, 'rb'))



def predict_health(temperature, humidity):
	# my_sample = np.array([24, 80]).reshape(1, -1)
	my_sample = np.array([temperature, humidity]).reshape(1, -1)

	prediction = model.predict(my_sample)

	print("PREDICTION:", prediction)
	return prediction

