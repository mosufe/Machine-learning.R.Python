#Polinomial regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import dataset and store it in two separate vectors
dataset = pd.read_csv('./B-Regressions/PolinomialLinearRegression/data/Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values #Matrix of features - Always treat the feature matrix as a matrix doing 1:2 and not just 1
y = dataset.iloc[:, 2].values #Dependent variables set

#Split the dataset into Training set and a Test set
"""from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)"""

#Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
print(x_train)
print(x_test)"""

#Fitting regression model to the dataset
#Create regressor

#Predicting a new result with Polinomial Regression
y_pred = regressor.predict(6.5)

#Visualizing the polinomial regression results
plt.scatter(x, y, color = 'red')
plt.plot(x, regressor.predict(x), color = 'blue')
plt.title('Truth or Bluff (Polinomial regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Visualizing the polinomial regression results with higher resolution
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))#Reshapes the whole x plot to avoit straight lines between points and increase precison

plt.scatter(x, y, color = 'red')
plt.plot(x, regressor.predict(x), color = 'blue')
plt.title('Truth or Bluff (Polinomial regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()