#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import sklearn
import random


data = pd.read_csv("datasets/dhtreadings.csv")

data = data.iloc[:, 1:3]

data

data = data.sort_values('temperature')


arr = []
for i in range(len(data)):
    if i <= len(data) // 3:
        arr.append(1)
    elif len(data) // 3 < i <= 2*len(data) // 3:
        arr.append(2)
    elif i > 2*len(data) // 3:
        arr.append(3)
arr_np = np.array(arr)
arr_np = arr_np.reshape((len(data), 1))


data_np = data.to_numpy()


data_new = np.append(data_np, arr_np, axis = 1)


from sklearn.utils import shuffle
data_new = shuffle(data_new)


data_new


random_ind = np.random.choice([0, 1], size = data_new.shape[0], p = [0.2, 0.8]).astype('bool')
train_data = data_new[random_ind]
test_data = data_new[(1-random_ind).astype('bool')]
x_train = train_data[:, :2]
y_train = train_data[:, 2]
x_test = test_data[:, :2]
y_test = test_data[:, 2]


from sklearn.tree import DecisionTreeClassifier
classifier_decision = DecisionTreeClassifier()
classifier_decision.fit(x_train, y_train)


y_pred = classifier_decision.predict(x_test)
print(y_pred)


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))



from sklearn.ensemble import RandomForestClassifier
classifier_random = RandomForestClassifier()
classifier_random.fit(x_train, y_train)



y_pred = classifier_random.predict(x_test)
print(y_pred)


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))



from sklearn.neighbors import KNeighborsClassifier
classifier_knn = KNeighborsClassifier()
classifier_knn.fit(x_train, y_train)



y_pred = classifier_knn.predict(x_test)



print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))



from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(C=1e5)

# Create an instance of Logistic Regression Classifier and fit the data.
logreg.fit(x_train, y_train)



y_pred = logreg.predict(x_test)



print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))



my_sample = np.array([24, 80]).reshape(1, -1)



y_pred_1 = logreg.predict(my_sample)
print(y_pred_1)


# Save last model - logreg
import pickle

filename = 'models/logreg_model.sav'
pickle.dump(logreg, open(filename, 'wb'))

# s = pickle.dumps(logreg)
# To use model:
# model = pickle.loads(s)


