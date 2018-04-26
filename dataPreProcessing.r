dataset = read.csv('data/Data.csv')

dataset$Age = ifelse(is.na(dataset$Age), #Verifies if the field age is empty
                    ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),#if the condition is true, replace by columns mean
                    dataset$Age)#if the condition is false keep the value

dataset$Salary = ifelse(is.na(dataset$Salary), #Verifies if the field age is empty
                    ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),#if the condition is true, replace by columns mean
                    dataset$Salary)#if the condition is false keep the value

#Encoding non numerical data
dataset$Country = factor(dataset$Country,
                        levels = c('France','Spain','Germany'),
                        labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased,
                        levels = c('No','Yes'),
                        labels = c(0, 1))

#Splitting the dataset into Training set and Test set
# install.packages('caTools')
library('caTools')
set.seed(123)#Forces same results
split = sample.split(dataset$Purchased, SplitRatio = 0.8) #Splits data into categories true and false

training_set = subset(dataset, split == TRUE) #recieves the subset of datasat containing true
test_set = subset(dataset, split == FALSE) #recieves the subset of datasat containing false
print(training_set)
print(test_set)