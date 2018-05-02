dataset = read.csv('./B-Regressions/SimpleLinearRegression/data/Salary_Data.csv')
# dataset = dataset[, 2:3]

#Splitting the dataset into Training set and Test set
library('caTools')
set.seed(123) #Forces same results
split = sample.split(dataset$Salary, SplitRatio = 2/3) #Splits data into categories true and false

training_set = subset(dataset, split == TRUE) #recieves the subset of datasat containing true
test_set = subset(dataset, split == FALSE) #recieves the subset of datasat containing false

#Feature Scaling
#The first and last columns arent numeric so we need to scale only numbers
# training_set[, 2:3] = scale(training_set[, 2:3])#Scales only columns 2 and 3
# test_set[, 2:3] = scale(test_set[, 2:3])#Scales only columns 2 and 3


#Fitting Simple linear regression to the training set
regressor = lm(formula = Salary ~ YearsExperience, #Creates a formula saying that salary is proportional to Years of Experience
                data = training_set)#set used to build the model

#summary(regressor) #tells you the values of your model coeficients

#Predictimg the test set results
y_pred = predict(regressor, newdata = test_set) #Takes as parameters the regression relations and the set in which the model will be applied

#Visualizing the Training set results
# install.packages('ggplot2')
library(ggplot2)
ggplot() + 
    geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
      colour = 'red') +
    geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
    colour = 'blue') +
    ggtitle('Salary vs Experience (Training Set)') +
    xlab('Years of experience') +
    ylab('Salary')        


#Visualizing the test set results
# install.packages('ggplot2')
library(ggplot2)
ggplot() + 
    geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
      colour = 'red') +
    geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
    colour = 'blue') +
    ggtitle('Salary vs Experience (Test Set)') +
    xlab('Years of experience') +
    ylab('Salary')  

# print(training_set)
# print(test_set)