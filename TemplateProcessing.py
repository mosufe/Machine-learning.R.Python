import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import dataset and store it in two separate vectors
dataset = pd.read_csv('data/Data.csv')
x = dataset.iloc[:, :-1].values #Matrix of features
y = dataset.iloc[:, 3].values #Dependent variables set

#Split the dataset into Training set and a Test set
#The training set is the set the machine learning model uses to learn
#The test set is the set used to validate if the machine learning model did indeed learn
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#Feature scaling
#transforms every single column to a range of -1 and 1
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
print(x_train)
print(x_test)"""

print(x)
print(y)