import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import dataset and store it in two separate vectors
dataset = pd.read_csv('./B-Regressions/data/Salary_Data.csv')
x = dataset.iloc[:, :-1].values #Matrix of features
y = dataset.iloc[:, 1].values #Dependent variables set

#Split the dataset into Training set and a Test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

#Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
print(x_train)
print(x_test)"""

#Fitting Simple linear regression for the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#This line learns the correlation between the features and dependant data
regressor.fit(x_train, y_train)# features x/dependat variables y

#Predicting the Test set results
y_pred = regressor.predict(x_test)#Creates a vector of predictions
 
#Visualizing the training set result
plt.scatter(x_train, y_train, color = 'red')#plots the points of the training set in red
plt.plot(x_train, regressor.predict(x_train), color = 'blue')#plots the predicted regression y points
plt.title('Salary vs Experience (TRAINING SET)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

#Visualizing the test set results
plt.scatter(x_test, y_test, color = 'red') #plots the points of the training set in red
plt.plot(x_train, regressor.predict(x_train), color = 'green') #plots the predicted regression y points
plt.title('Salary vs Experience (TEST SET)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()


# print(y_test)
# print(y_pred)

# print(x)
# print(y)
# print(x_train)
# print(y_train)

# print(x_test)
# print(y_test)
