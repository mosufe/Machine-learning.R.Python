#Regression template

#======================================== Preprocessing Phase ========================================================
dataset = read.csv('./B-Regressions/PolinomialLinearRegression/data/Position_Salaries.csv')
dataset = dataset[2:3]

#Splitting the dataset into Training set and Test set
# install.packages('caTools')
# library('caTools')
# set.seed(123)#Forces same results
# split = sample.split(dataset$Purchased, SplitRatio = 0.8) #Splits data into categories true and false
# training_set = subset(dataset, split == TRUE) #recieves the subset of datasat containing true
# test_set = subset(dataset, split == FALSE) #recieves the subset of datasat containing false

#Feature Scaling
#The first and last columns arent numeric so we need to scale only numbers
# training_set[, 2:3] = scale(training_set[, 2:3])#Scales only columns 2 and 3
# test_set[, 2:3] = scale(test_set[, 2:3])#Scales only columns 2 and 3


#======================================== Creating the model ========================================================
#Fitting the polynomial regression to the dataset
#Create your regressor here

#Predicting a new result
y_pred = predict(regressor, data.frame(Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3, Level4 = 6.5^4))
print(y_pred)

#Visualizing the regression model Results
#install.packages('ggplot2')
library('ggplot2')
ggplot() +
    geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
    geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), color = 'blue') +
    ggtitle('Truth or Bluff (Linear Regression)') + 
    xlab('Level') + 
    ylab('Salary')

#Visualizing the regression model (with higher resolution)
#install.packages('ggplot2')
library('ggplot2')
x_grid = seq(min(dataset$Level),max(dataset$Level), 0.1)
ggplot() +
    geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
    geom_line(aes(x = x_grid$Level, y = predict(regressor, newdata = data.frame(Level = x_grid))), color = 'blue') +
    ggtitle('Truth or Bluff (Linear Regression)') + 
    xlab('Level') + 
    ylab('Salary')


