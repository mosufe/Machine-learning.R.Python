import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import dataset and store it in two separate vectors
dataset = pd.read_csv('./A-PreprocessingSteps/data/Data.csv')
x = dataset.iloc[:, :-1].values #Matrix of features
y = dataset.iloc[:, 3].values #Dependent variables set

#Treat missing fields replacing them by the row's mean
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN',strategy = 'mean', axis = 0) #Defines the imputer strategy
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3]) #Replaces the missing data

#Encoding non numerical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le_x = LabelEncoder()#Associates country names to numerical labels
x[:, 0] = le_x.fit_transform(x[:, 0])#Applies the transformation to the first column only

ohe = OneHotEncoder(categorical_features=[0])#Dummy variables, prevents the algorithm to order the data as for ex France > Germany
x = ohe.fit_transform(x).toarray()

le_y = LabelEncoder()#Associates country names to numerical labels
y = le_y.fit_transform(y)#Applies the transformation to the first column only

#Split the dataset into Training set and a Test set
#The training set is the set the machine learning model uses to learn
#The test set is the set used to validate if the machine learning model did indeed learn
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#Feature scaling
#transforms every single column to a range of -1 and 1
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
print(x_train)
print(x_test)

print(x)
print(y)