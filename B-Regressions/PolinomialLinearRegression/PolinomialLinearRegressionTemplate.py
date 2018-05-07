#Polinomial regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import dataset and store it in two separate vectors
dataset = pd.read_csv('./B-Regressions/PolinomialLinearRegression/data/Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values #Matrix of features - Always treat the feature matrix as a matrix doing 1:2 and not just 1
y = dataset.iloc[:, 2].values #Dependent variables set

#Fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y) 

#Fitting polynomnial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)#Changing the degree aproximates the results better
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

#Visualizing the linear regression results
plt.scatter(x, y, color = 'red')
plt.plot(x,lin_reg.predict(x), color = 'blue')
plt.title('Truth or Bluff (Linear regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Visualizing the polinomial regression results
plt.scatter(x, y, color = 'red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.title('Truth or Bluff (Polinomial regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Visualizing the polinomial regression results with better arccuracy
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)#Reshapes the whole x plot to avoit straight lines between points and increase precison

plt.scatter(x, y, color = 'red')
plt.plot(x_grid,lin_reg_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
plt.title('Truth or Bluff (Polinomial regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Predicting a new result with Linear Regression
print(lin_reg.predict(6.5))

#Predicting a new result with Polinomial Regression
print(lin_reg_2.predict(poly_reg.fit_transform(6.5)))