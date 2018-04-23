import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data/Data.csv')
x = dataset.iloc[:, :-1].values #Matrix of features
y = dataset.iloc[:, 3].values #Dependent variables set

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN',strategy = 'mean', axis = 0) #Defines the imputer strategy
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3]) #Replaces the missing data
