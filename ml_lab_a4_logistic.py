# -*- coding: utf-8 -*-
"""ML_Lab_A4_Logistic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mVYeuufXeDft39xyIKFsgu62iWX7oNTO

# **MACHINE LEARNING LAB - 4**

# **Problem Statement : Implement of Logistic Regression Algorithm**

**Import Libraries**
"""

from sklearn.model_selection import train_test_split
from sklearn.datasets import *
from sklearn.linear_model import LogisticRegression

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

"""**Load the data**"""

data = load_breast_cancer() #refer: http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer

# data with features
X = data.data

# data class labels
y = data.target

print(X.shape,X[:1])

print(y.shape,y)

"""**Print the number of data points, number of features and number of classes in the given data set.**"""

features = len(X[0])
print("Data point " ,len(X))
print("features ",features)
print("number of class",len(set(y)))

"""**Splitting data into Train and test sets with Stratified Sampling using train_test_split()**"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
print(len(X_train),len(X_test),len(y_train),len(y_test))

"""**Data Preprocessing using column standardisation. Use sklearn.preprocessing.StandardScaler().**"""

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled =scaler.transform(X_test)

print(X_train_scaled[:1])

"""## **Implement Logistic Regression Using Gradient Descent: without using sklearn.**

In this algorithm, $n$ is the total number of datapoints in dataset. 
$\alpha$ is the learning rate to be used in gradient descent. For this work, just fix $\alpha = 0.001$.

The predicted value for data point $x$ is $y_{pred} = σ(w^{T}x + b)$, where $σ$ is a sigmoid function.

**ALGORITHM:**

<br>

* Initialize the weight_vector and intercept term to zeros (Write your code in <font color='blue'>def initialize_weights()</font>)

* Create a loss function (Write your code in <font color='blue'>def logloss()</font>) 

 $log loss = -1*\frac{1}{n}\Sigma_{for each y_{true},y_{pred}}(y_{true}log(y_{pred})+(1-y_{true})log(1-y_{pred}))$
- for each epoch:

    - for each data point say $x_{i}$ in train:

        - calculate the gradient of loss function w.r.t each weight in weight vector (write your code in <font color='blue'>def gradient_dw()</font>)

        $dw^{(t)} = \frac{1}{n}(x_i(σ((w^{(t)})^{T} x_i+b^{t}) - y_i))$ <br>

        - Calculate the gradient of the intercept (write your code in <font color='blue'> def gradient_db()</font>)

           $ db^{(t)} = \frac{1}{n}(σ((w^{(t)})^{T} x_i+b^{t}) - y_i))$

        - Update weights and intercept usign gradient descent  <br>
        $w^{(t+1)}← w^{(t)} - α(dw^{(t)}) $<br>

        $b^{(t+1)}←b^{(t)} - α(db^{(t)}) $
    - predict the output for all test data points with updated weights. (write your function in def prediction())
    - calculate the log loss for train and test data points separately with the updated weights. Store these losses in the lists, train_loss and test_loss.
    - And if you wish, you can compare the previous train loss and the current train loss, if it is not updating, then
        you can stop the training
    -return the updated weights, training and test loss lists.
"""

n_features = len(X[0])

def initialize_weights():
    weights = np.zeros((n_features, ))
    bias = 0
    return weights, bias

def sigmoid(z):
  return 1 / (1 + np.exp(-z))

def logloss(y_true, y_pred):
   n = y_true.shape[0]
   log_sum = 0
   
   for i in range(n):
     log_sum += (y_true[i] * np.log(y_pred[i])) + ((1 - y_true[i]) * np.log(1 - y_pred[i]))
    
   return -log_sum / n
    # you have been given two arrays y_true and y_pred and you have to calculate the logloss

# w should be a vector of size as input data point. Size of w and dw be same.
def gradient_dw(x, y, w, b):
  dw = np.dot(x, sigmoid(np.dot(w.T, x) + b) - y)
  return dw

#b should be a scalar value
def gradient_db(x,y,w,b):
  db = sigmoid(np.dot(w.T, x) + b) - y
  return db

"""**For the prediction, if activation_value > 0.5 then assign label = 1 else label = 0**"""

def predict(x, w, b):
 predictions = []
 for point in x:
   predictions.append(0 if sigmoid(np.dot(w.T, point) + b) < 0.5 else 1)
 return predictions

def logistic_regression(epochs=1000, alpha=.001):
    weights, bias = initialize_weights()
    n = len(X_train_scaled[0])
    train_loss = []

    for epoch in range(epochs):
        for x, y in zip(X_train_scaled, y_train):
            weights -= (alpha * gradient_dw(x, y, weights, bias))
            bias -= (alpha * gradient_db(x, y, weights, bias))
        loss = logloss(y_train, sigmoid(np.dot(X_train_scaled, weights) + bias))
        train_loss.append(loss)
    return weights, bias, train_loss

"""**Plot your train and test loss vs epochs. Plot epoch number on X-axis and loss on Y-axis and make sure that the curve is converging**"""

weights, bias, train_loss = logistic_regression()

plt.plot(list(range(1000)), train_loss)

"""**BONUS: Train your model with varying values of learning rates say ranging in $[0.1, 0.01, 0.001, 0.0001]$ and plot the performances.**"""

y_pred = predict(X_test_scaled, weights, bias)
accuracy = accuracy_score(y_test, y_pred)

alpha_list = [0.1, 0.01, 0.001, 0.0001]
acc_list = []

for alpha in alpha_list:
    weights, bias, train_loss = logistic_regression(alpha=alpha)
    y_pred = predict(X_test_scaled, weights, bias)
    accuracy = accuracy_score(y_test, y_pred)
    acc_list.append(accuracy)

print(list(zip(alpha_list, acc_list)))

plt.scatter([str(x) for x in alpha_list], acc_list)