# -*- coding: utf-8 -*-
from sklearn.neural_network import MLPRegressor
import numpy as np
from sklearn import preprocessing
x_train1 = np.loadtxt("./train_data.txt") #input data
x_test = np.loadtxt("./test_data.txt")
y_train = np.loadtxt("./train_truth.txt")
# print(y_train)
scaler = preprocessing.StandardScaler().fit(x_train1) # data standardization
x_train = scaler.transform(x_train1)
scaler = preprocessing.StandardScaler().fit(x_test)
x_test = scaler.transform(x_test)
y_train.reshape(-1,1) # sklearn only accepts 2-dimensional data


mlp = MLPRegressor(
    hidden_layer_sizes=(6,2),  activation='relu', solver='adam', alpha=0.0001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False,beta_1=0.9, beta_2=0.999, epsilon=1e-08)
mlp.fit(x_train, y_train) # train
mlp_score=mlp.score(x_train,y_train) #score
print('mlp_score',mlp_score)

from sklearn.model_selection import cross_val_score

scores = cross_val_score(mlp, x_train, y_train, cv=5) #cross-validation
print(scores)



result = mlp.predict(x_test) # predict
print(result)
np.savetxt('test_predicted_3.txt',result)
