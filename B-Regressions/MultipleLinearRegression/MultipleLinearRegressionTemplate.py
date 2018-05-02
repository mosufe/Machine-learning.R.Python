import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import dataset and store it in two separate vectors
dataset = pd.read_csv('./B-Regressions/MultipleLinearRegression/data/50_Startups.csv')
x = dataset.iloc[:, :-1].values #Matrix of features
y = dataset.iloc[:, 4].values #Dependent variables set

#Encoding non numerical data into numbers
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le_x = LabelEncoder()#Associates country names to numerical labels
x[:, 3] = le_x.fit_transform(x[:, 3])#Applies the transformation

ohe = OneHotEncoder(categorical_features=[3])#Dummy variables, prevents the algorithm to order the data as for ex France > Germany
x = ohe.fit_transform(x).toarray()

#Avoiding Dummy variable Trap
x = x[:, 1:]#Removes the first column of x

#Split the dataset into Training set and a Test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
print(x_train)
print(x_test)"""

#Fitting Multiple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Predicting the Test set results
y_pred = regressor.predict(x_test)

print(y_test)
print(y_pred)

