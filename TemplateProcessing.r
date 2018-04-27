dataset = read.csv('data/Data.csv')
# dataset = dataset[, 2:3]

#Splitting the dataset into Training set and Test set
# install.packages('caTools')
library('caTools')
set.seed(123)#Forces same results
split = sample.split(dataset$Purchased, SplitRatio = 0.8) #Splits data into categories true and false

training_set = subset(dataset, split == TRUE) #recieves the subset of datasat containing true
test_set = subset(dataset, split == FALSE) #recieves the subset of datasat containing false

#Feature Scaling
#The first and last columns arent numeric so we need to scale only numbers
# training_set[, 2:3] = scale(training_set[, 2:3])#Scales only columns 2 and 3
# test_set[, 2:3] = scale(test_set[, 2:3])#Scales only columns 2 and 3



print(training_set)
print(test_set)