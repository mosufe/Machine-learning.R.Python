dataset = read.csv('./B-Regressions/MultipleLinearRegression/data/50_Startups.csv')

#Encoding non numerical data
dataset$State = factor(dataset$State,
                        levels = c('New York','California','Florida'),
                        labels = c(1, 2, 3))

#Splitting the dataset into Training set and Test set
# install.packages('caTools')
library('caTools')
set.seed(123)#Forces same results
split = sample.split(dataset$Profit, SplitRatio = 0.8) #Splits data into categories true and false

training_set = subset(dataset, split == TRUE) #recieves the subset of datasat containing true
test_set = subset(dataset, split == FALSE) #recieves the subset of datasat containing false

#Fitting multiple linear regression to the training set
# regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State)
# regressor = lm(formula = Profit ~ .,
#                 data = training_set)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = dataset)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, data = dataset)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, data = dataset)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend, data = dataset)
summary(regressor)

#Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# print(y_pred)
# print(test_set)
