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

# print(x)
# print(y)
# print(x_train)
# print(y_train)

# print(x_test)
# print(y_test)
