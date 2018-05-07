dataset = read.csv('./B-Regressions/PolinomialLinearRegression/data/Position_Salaries.csv')
dataset = dataset[2:3]

#Fitting the linear regression to the dataset
lin_reg = lm(formula = Salary ~ ., data = dataset)

#Fitting the polynomial regression to the dataset
dataset$Level2 = dataset$Level^2 #Creates a new column in dataset containing the levels squared
dataset$Level3 = dataset$Level^3 #Creates a new column in dataset containing the levels tripled
dataset$Level4 = dataset$Level^4 #Creates a new column in dataset containing the levels quadrupled
poly_reg = lm(formula = Salary ~ ., data = dataset)

#Visualizing the linear regression Results
#install.packages('ggplot2')
library('ggplot2')
ggplot() +
    geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
    geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)), color = 'blue') +
    ggtitle('Truth or Bluff (Linear Regression)') + 
    xlab('Level') + 
    ylab('Salary')

#Visualizing the polynomial regression Results
#install.packages('ggplot2')
library('ggplot2')
ggplot() +
    geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
    geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)), color = 'blue') +
    ggtitle('Truth or Bluff (Linear Regression)') + 
    xlab('Level') + 
    ylab('Salary')

#Predicting a new result with linear regression
y_pred = predict(lin_reg, data.frame(Level = 6.5))
print(y_pred)

#Predicting a new result with polynomial regression
y2_pred = predict(poly_reg, data.frame(Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3, Level4 = 6.5^4))
print(y2_pred)


